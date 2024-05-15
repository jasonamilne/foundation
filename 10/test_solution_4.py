from solution import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_findMedianSortedArrays_single_element_each(solution):
    """Test with one element in each array."""
    nums1 = [1]
    nums2 = [2]
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.5

def test_findMedianSortedArrays_same_length(solution):
    """Test with two arrays of the same length."""
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5

def test_findMedianSortedArrays_different_length(solution):
    """Test with two arrays of different lengths."""
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6]
    assert solution.findMedianSortedArrays(nums1, nums2) == 3.5

def test_findMedianSortedArrays_empty_first_array(solution):
    """Test with an empty first array."""
    nums1 = []
    nums2 = [1, 2, 3, 4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5

def test_findMedianSortedArrays_empty_second_array(solution):
    """Test with an empty second array."""
    nums1 = [1, 2, 3, 4]
    nums2 = []
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5

def test_findMedianSortedArrays_both_empty(solution):
    """Test with both arrays empty."""
    nums1 = []
    nums2 = []
    with pytest.raises(ValueError):
        solution.findMedianSortedArrays(nums1, nums2)

def test_findMedianSortedArrays_large_arrays(solution):
    """Test with large arrays."""
    nums1 = list(range(1, 10001))
    nums2 = list(range(10001, 20001))
    assert solution.findMedianSortedArrays(nums1, nums2) == 10000.5

def test_findMedianSortedArrays_overlapping_elements(solution):
    """Test with overlapping elements (duplicates allowed)."""
    nums1 = [1, 2, 6]
    nums2 = [2, 3, 4, 5]
    assert solution.findMedianSortedArrays(nums1, nums2) == 3 
