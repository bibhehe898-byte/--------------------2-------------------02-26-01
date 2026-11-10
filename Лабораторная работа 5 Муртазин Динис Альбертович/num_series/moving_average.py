"""Скользящие средние: SMA, CMA, EMA."""
from typing import List, Sequence


def _check_window(window: int, n: int) -> None:
    """Проверяем окно."""
    if not isinstance(window, int) or window < 1:
        raise ValueError(f"window должно быть целым >= 1 (получено: {window!r})")
    if window > n:
        raise ValueError(f"window ({window}) не может быть больше длины ряда ({n})")


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму — O(n)."""
    if not data:
        raise ValueError("Ряд пуст")
    _check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]

    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)

    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA — окно должно быть нечётным."""
    if not data:
        raise ValueError("Ряд пуст")
    if window % 2 == 0:
        raise ValueError(f"Для центрированного MA window должно быть нечётным (получено: {window})")
    _check_window(window, len(data))

    sma = simple_moving_average(data, window)
    half = window // 2
    # SMA[i] соответствует центру i+half в исходном ряде
    # Сдвигаем: первые и последние half точек "не имеют центра"
    return [sma[i] for i in range(len(sma))]


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha*data[i] + (1-alpha)*EMA[i-1]."""
    if not data:
        raise ValueError("Ряд пуст")
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должно быть в (0, 1] (получено: {alpha})")

    ema = [float(data[0])]
    for i in range(1, len(data)):
        ema.append(alpha * data[i] + (1 - alpha) * ema[i - 1])
    return ema