from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

# Test normal cases functionality
def test_findMedianSortedArrays_normal_cases(solution):
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert solution.findMedianSortedArrays([2], []) == 2.0

# Test edge cases functionality
def test_findMedianSortedArrays_edge_cases(solution):
    assert solution.findMedianSortedArrays([], []) == 0.0
    assert solution.findMedianSortedArrays([1], []) == 1.0

# Test special cases functionality
def test_findMedianSortedArrays_special_cases(solution):
    assert solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6]) == 3.5
    assert solution.findMedianSortedArrays([1, 3], [2, 4, 5]) == 3.0

# Test performance cases functionality
def test_findMedianSortedArrays_performance_cases(solution):
    large_array1 = list(range(10000))
    large_array2 = list(range(10000, 20000))
    assert solution.findMedianSortedArrays(large_array1, large_array2) == 9999.5

