from typing import List, Optional, Tuple
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height is None:
            raise ValueError("Invalid input: None")
        if len(height) < 2:
            raise ValueError("Invalid input: Array length must be at least 2")

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
    def intToRoman(self, num: int) -> str:
        return

    def romanToInt(self, s: str) -> int:
        return

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return

    def letterCombinations(self, digits: str) -> List[str]:
        return

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return

    def isValid(self, s: str) -> bool:
        return
