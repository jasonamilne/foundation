import pytest

class Solution():
    def find_max(self, nums: list[int]) -> int:
        """
        Psuedocode:
        1. if nums is empty, return None
        2. enumerate nums
        3. if i == 0, set maxNum = num (first element)
        4. if num > maxNum, set maxNum = num (2 to last element)
        5. return maxNum
        """
        if not nums:
            return None
        for i, num in enumerate(nums):
            if i == 0:
                maxNum = num
            elif num > maxNum:
                maxNum = num
        return maxNum
