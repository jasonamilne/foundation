from typing import List

class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays.

        Pseudocode:
        1. Merge the two arrays.
        2. Sort the merged array.
        3. Calculate the number of elements in the merged array.
        4. If the number of elements is odd, return the middle element.
        5. If the number of elements is even, return the average of the two middle elements.

        Time complexity: O((m+n) log(m+n)) - due to sorting the merged array
        Space complexity: O(m+n) - to store the merged array
        Algorithm: Merge and Sort

        Args:
            nums1 (List[int]): The first sorted array.
            nums2 (List[int]): The second sorted array.

        Returns:
            float: The median of the two sorted arrays.

        Examples:
            >>> solution = Solution()
            >>> solution.findMedianSortedArrays([1, 3], [2])
            2.0
            >>> solution.findMedianSortedArrays([1, 2], [3, 4])
            2.5
            >>> solution.findMedianSortedArrays([0, 0], [0, 0])
            0.0
            >>> solution.findMedianSortedArrays([], [1])
            1.0
            >>> solution.findMedianSortedArrays([2], [])
            2.0
        """
        if not nums1 and not nums2:
            return 0.0
        # Merge the arrays into a single sorted array
        merged = nums1 + nums2
        # Sort the merged array
        merged.sort()
        # Calculate the number of elements in the merged array
        n = len(merged)
        # If the number of elements is odd, return the middle element
        if n % 2 == 1:
            return float(merged[n // 2])
        # If the number of elements is even, return the average of the two middle elements
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
