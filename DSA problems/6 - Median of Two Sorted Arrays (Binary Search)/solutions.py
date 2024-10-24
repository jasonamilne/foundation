from typing import List

class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays using binary search.

        Pseudocode:
        1. Ensure the first array is the smaller one for efficiency.
        2. Calculate the total length of both arrays.
        3. Use binary search on the smaller array to find the correct partition.
        4. Compare elements around the partition to determine if it's correct.
        5. If correct, calculate the median based on the total length (odd/even).
        6. Adjust the binary search range based on comparisons.

        Time complexity: O(log(min(n1, n2)))
        Space complexity: O(1)
        Algorithm: Binary Search

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
        n1 = len(nums1)
        n2 = len(nums2)
        if not nums1 and not nums2:
            return 0.0
        
        # Ensure nums1 is the smaller array for efficiency
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # Calculate total length and partition point
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low = 0
        high = n1
        
        # Binary search on nums1 to find the correct partition
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            # Compare elements around the partition
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            # Check if the partition is correct
            if l1 <= r2 and l2 <= r1:
                # If correct partition, calculate median
                if n % 2 == 1:
                    # If odd, return the max of the left elements
                    return max(l1, l2)
                else:
                    # If even, return the average of the max of the left elements 
                    # and the min of the right elements
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # If partition is incorrect, adjust the search range
                high = mid1 - 1
            else:
                # If partition is incorrect, adjust the search range
                low = mid1 + 1
        # If no correct partition is found, return 0
        return 0
