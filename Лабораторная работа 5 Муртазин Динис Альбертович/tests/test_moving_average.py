import pytest
from num_series import (
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
)


def test_sma_basic():
    assert simple_moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]


def test_sma_window_1():
    assert simple_moving_average([1, 2, 3], 1) == [1.0, 2.0, 3.0]


def test_sma_window_eq_len():
    assert simple_moving_average([1, 2, 3], 3) == [2.0]


def test_sma_too_big():
    with pytest.raises(ValueError):
        simple_moving_average([1, 2], 5)


def test_sma_bad_window():
    with pytest.raises(ValueError):
        simple_moving_average([1, 2, 3], 0)


def test_ema():
    ema = exponential_moving_average([1, 1, 1], 0.5)
    assert ema == [1.0, 1.0, 1.0]


