import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_two_sum_basic(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_multiple_pairs(solution):
    result = solution.twoSum([3, 2, 4], 6)
    assert result == [1, 2] or result == [2, 1]

def test_two_sum_no_pair(solution):
    assert solution.twoSum([1, 2, 3], 7) == []

def test_two_sum_negative_numbers(solution):
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_duplicates(solution):
    assert solution.twoSum([3, 3], 6) == [0, 1]

def test_two_sum_large_numbers(solution):
    assert solution.twoSum([1000000000, 300000000, 700000000], 1000000000) == [1, 2]
