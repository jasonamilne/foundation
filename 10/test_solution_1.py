from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_twoSum_basic_case(solution):
    """Test basic case with a single valid pair"""
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_twoSum_multiple_pairs(solution):
    """Test case where multiple pairs can sum to target"""
    result = solution.twoSum([3, 2, 4], 6)
    assert result == [1, 2] or result == [2, 1]

def test_twoSum_no_valid_pair(solution):
    """Test case where no pairs sum to target"""
    assert solution.twoSum([1, 2, 3], 7) == []

def test_twoSum_with_negative_numbers(solution):
    """Test case with negative numbers in the array"""
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_twoSum_with_duplicates(solution):
    """Test case where input array contains duplicates"""
    assert solution.twoSum([3, 3], 6) == [0, 1]

def test_twoSum_with_large_numbers(solution):
    """Test case with large numbers in the array"""
    assert solution.twoSum([1000000000, 300000000, 700000000], 1000000000) == [1, 2]
