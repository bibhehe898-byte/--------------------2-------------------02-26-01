import pytest
from num_series import random_series, sine_series, trend_series


def test_random_len():
    assert len(random_series(10, seed=1)) == 10
    assert len(random_series(5, seed=42)) == 5


def test_random_reproducible():
    a = random_series(5, seed=42)
    b = random_series(5, seed=42)
    assert a == b  # с одним и тем же seed результат одинаковый


def test_random_bad_n():
    with pytest.raises(ValueError):
        random_series(-1)
    with pytest.raises(ValueError):
        random_series(0)


def test_random_bad_range():
    with pytest.raises(ValueError):
        random_series(5, low=10, high=0)


def test_sine_len():
    assert len(sine_series(20, seed=1)) == 20


def test_trend():
    assert trend_series(5, start=0, step=1, noise=0) == [0, 1, 2, 3, 4]
    assert trend_series(3, start=10, step=2, noise=0) == [10, 12, 14]