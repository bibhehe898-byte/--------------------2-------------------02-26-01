import pytest
from num_series import mean, median, spread, summarize


def test_mean():
    assert mean([1, 2, 3]) == 2.0
    assert mean([10, 20, 30, 40]) == 25.0


def test_median_odd():
    assert median([3, 1, 2]) == 2.0
    assert median([5, 3, 1, 4, 2]) == 3.0


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5
    assert median([10, 20, 30, 40]) == 25.0


def test_spread():
    assert spread([5, 1, 10]) == 9.0
    assert spread([-5, 5]) == 10.0


def test_empty():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        spread([])


def test_summarize():
    s = summarize([1, 2, 3, 4])
    assert s["count"] == 4
    assert s["mean"] == 2.5
    assert s["median"] == 2.5
    assert s["spread"] == 3.0
    assert s["min"] == 1.0
    assert s["max"] == 4.0