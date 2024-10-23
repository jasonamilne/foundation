import pytest

class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Psuedocode:
        1. enumerate nums
        2. for i in range(len(nums)):
        3. for j in range(i+1, len(nums)):
        4. if nums[i] + nums[j] == target:
        5. return [i, j]
        6. return []

        Time complexity: O(n^2)
        Space complexity: O(1)  
        Algorithm: Brute force
        """
        if type(nums) != list or not all(isinstance(x, int) for x in nums) or type(target) != int or len(nums) < 2:
            raise ValueError("Input must be a list of integers")
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
