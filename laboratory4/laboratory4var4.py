import math


def read_float(prompt, min_val, max_val):
    """Ввод вещественного числа с проверкой типа и диапазона."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Ошибка: введите число (например, 12.5). Повторите ввод.")
            continue
        if value < min_val or value > max_val:
            print(f"  Ошибка: значение должно быть в диапазоне {min_val}..{max_val}. Повторите ввод.")
            continue
        return value


def area_circle(d_mm):
    """Площадь круга, м^2. d_mm — диаметр в мм."""
    d_m = d_mm / 1000.0
    return math.pi * d_m ** 2 / 4.0

def area_rect(a_mm, b_mm):
    """Площадь прямоугольника, м^2."""
    a_m = a_mm / 1000.0
    b_m = b_mm / 1000.0
    return a_m * b_m

def area_ring(D_mm, d_mm):
    """Площадь кольца, м^2. D_mm — наружный, d_mm — внутренний диаметр."""
    D_m = D_mm / 1000.0
    d_m = d_mm / 1000.0
    return math.pi * (D_m ** 2 - d_m ** 2) / 4.0

def flow_rate(area_m2, v_ms):
    """Расход, м^3/ч. area_m2 — площадь м^2, v_ms — скорость м/с."""
    return area_m2 * v_ms * 3600.0

def classify_circle(d_mm):
    """Класс сечения для круглого варианта (по диаметру)."""
    if d_mm < 25:
        return "малое сечение"
    elif d_mm <= 200:
        return "нормальное сечение"
    else:
        return "крупное сечение"

def main():
    print("=== Расчёт расхода жидкости через сечение трубопровода ===")
    print("Выберите тип сечения:")
    print("  1 — круглое")
    print("  2 — прямоугольное")
    print("  3 — кольцевое")

    while True:
        try:
            mode = int(input("Ваш выбор (1-3): "))
        except ValueError:
            print("  Ошибка: введите целое число 1, 2 или 3.")
            continue
        if mode not in (1, 2, 3):
            print("  Ошибка: выберите 1, 2 или 3.")
            continue
        break

    match mode:
        case 1:
            section_name = "круглое"
            d = read_float("Диаметр d, мм (5..500): ", 5, 500)
            A = area_circle(d)
            cls = classify_circle(d)
            extra = f"d = {d} мм"

        case 2:
            section_name = "прямоугольное"
            a = read_float("Сторона a, мм (5..500): ", 5, 500)
            b = read_float("Сторона b, мм (5..500): ", 5, 500)
            A = area_rect(a, b)
            h = min(a, b)
            cls = classify_circle(h)  # та же градация 25/200
            extra = f"a = {a} мм, b = {b} мм"

        case 3:
            section_name = "кольцевое"
            D = read_float("Наружный диаметр D, мм (5..500): ", 5, 500)
            while True:
                d = read_float("Внутренний диаметр d, мм (5..500): ", 5, 500)
                if d >= D:
                    print(f"  Ошибка: внутренний диаметр должен быть меньше наружного ({D} мм). Повторите ввод.")
                    continue
                break
            A = area_ring(D, d)
            cls = classify_circle(D)
            extra = f"D = {D} мм, d = {d} мм"

    v = read_float("Скорость потока v, м/с (0.1..10): ", 0.1, 10)

    Q = flow_rate(A, v)

    # Вывод
    print("\n--- Результаты ---")
    print(f"Тип сечения:        {section_name} ({extra})")
    print(f"Площадь сечения:    {A:.6f} м²")
    print(f"Скорость потока:    {v} м/с")
    print(f"Расход:             {Q:.3f} м³/ч")
    print(f"Класс сечения:      {cls}")


if __name__ == "__main__":
    main()