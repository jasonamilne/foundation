
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0


        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1

            # Update the last position of the character
            char_map[s[right]] = right  # O(1) update

            # Update the maximum length of the substring found
            max_length = max(max_length, right - left + 1)  # O(1) comparison and update

        # Return the maximum length of substring without repeating characters
        return max_length  # O(1)
