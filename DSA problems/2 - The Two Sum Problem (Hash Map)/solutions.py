from typing import List
import pytest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Psuedocode:
        1. enumerate nums
        2. for i, num in enumerate(nums):
        3. complement = target - num # memoization caches the complement efficiently
        4. if complement in complements:
        5. return [complements[complement], i]
        6. complements[num] = i # memoization caches the complement efficiently
        7. return []

        Time complexity: O(n)
        Space complexity: O(n)  
        Algorithm: Hash map
        """
        if type(nums) != list or not all(isinstance(x, int) for x in nums) or type(target) != int or len(nums) < 2:
            raise ValueError("Input must be a list of integers")
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i] # [a[i], a[j]]
            complements[num] = i
        return []
    
solution = Solution()
result = solution.twoSum([2,7,11,15], 9)
print(result)
