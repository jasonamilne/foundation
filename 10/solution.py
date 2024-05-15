from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` and an integer `target`, 
        return the indices of the two numbers such that they add up to `target`.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target integer.

        Returns:
            List[int]: Indices of the two numbers such that they add up to the target.
        
        Example:
            >>> solution = Solution()
            >>> solution.twoSum([2, 7, 11, 15], 9)
            [0, 1]
        
        Note:
            Each input will have exactly one solution. You may not use the same element twice.
        """
        
        # Brute force: O(n^2)
        """
        for i in range(len(nums)):  # O(n) - Iterates through the list once
            for j in range(i + 1, len(nums)):  # O(n) - Iterates through the remaining elements for each i
                if nums[i] + nums[j] == target:  # O(1) - Checks if the sum of the two elements is equal to the target
                    return [i, j]  # O(1) - Returns the indices if the condition is met
        return []  # O(1) - Returns an empty list if no pair is found
        """

        # Hash map: O(n)
        num_to_index = {}  # O(1) - Initializing an empty dictionary
        for i, num in enumerate(nums):  # O(n) - Iterating through the list once
            complement = target - num  # O(1) - Subtraction operation
            if complement in num_to_index:  # O(1) - Dictionary lookup
                return [num_to_index[complement], i]  # O(1) - Access and return
            num_to_index[num] = i  # O(1) - Dictionary insertion
        return []  # O(1) - Return statement
