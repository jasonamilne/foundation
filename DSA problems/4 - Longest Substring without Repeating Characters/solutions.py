from typing import Optional, List

class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Psuedocode:
        1. Initialize a char_map to store the last index of each character.
        2. Initialize left and max_length to 0.
        3. Iterate over the string with the right pointer.
        4. If the character is in char_map and its index is greater than or equal to left, update left.
        5. Update the char_map with the current character and its index.
        6. Update max_length with the maximum value between max_length and the distance between left and right plus one.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Performance:
            Time Complexity: O(n)
            Space Complexity: O(min(n, m)) where n is the length of the input string and m is the size of the character set.
            Algorithm: Sliding Window

        Examples:
        >>> solution = Solution()
        >>> solution.lengthOfLongestSubstring("abcabcbb")
        3
        >>> solution.lengthOfLongestSubstring("bbbbb")
        1
        >>> solution.lengthOfLongestSubstring("pwwkew")
        3
        """
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
