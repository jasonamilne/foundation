import pytest

class Solution():
    def find_max(self, nums: list[int]) -> int:
        """
        Psuedocode:
        1. Create a variable `maxNum` and initialize it to 0.
        2. Iterate over each element num in nums.
        3. If num is greater than `maxNum`, update `maxNum` = num.
        4. Output `maxNum`.
        """
        if not nums:
            return None
        for i, num in enumerate(nums):
            if i == 0:
                maxNum = num
            elif num > maxNum:
                maxNum = num
        return maxNum
