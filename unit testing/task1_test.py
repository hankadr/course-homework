import pytest

from task1 import IntegerSet

@pytest.mark.parametrize("numbers, expected_sum", [([1, 2, 3, 4, 5], 15),([10, 20, 30], 60),])
def test_sum_elements(numbers, expected_sum):
    assert IntegerSet(numbers).sum_elements() == expected_sum

@pytest.mark.parametrize("numbers, expected_mean", [([1, 2, 3, 4, 5], 3.0),([10, 20, 30], 20.0)])
def test_arithmetic_mean(numbers, expected_mean):
    assert IntegerSet(numbers).arithmetic_mean() == expected_mean

@pytest.mark.parametrize("numbers, expected_max", [([1, 2, 3, 4, 5], 5),([10, 20, 30], 30)])
def test_max_element(numbers, expected_max):
    assert IntegerSet(numbers).max_element() == expected_max

@pytest.mark.parametrize("numbers, expected_min", [([1, 2, 3, 4, 5], 1),([10, 20, 30], 10)])
def test_min_element(numbers, expected_min):
    assert IntegerSet(numbers).min_element() == expected_min

if __name__ == "__main__":
    pytest.main(["-v","--color=yes"])
