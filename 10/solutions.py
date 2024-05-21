from typing import List, Optional, Tuple
import pytest

class SearchAlgorithms:
    @staticmethod
    def binary_search_partition(nums1: List[int], nums2: List[int]) -> Tuple[int, int]:
        """
        Helper function to find the correct partition in the combined sorted arrays.

        Args:
            nums1 (List[int]): First sorted array.
            nums2 (List[int]): Second sorted array.


        Returns:
            Tuple[int, int]: The maximum of the left partition and the minimum of the right partition.
        """
        # Lengths of the two arrays
        m, n = len(nums1), len(nums2) # O(1)

        imin, imax, half_len = 0, m, (m + n + 1) // 2 # O(1)

        while imin <= imax:
            i = (imin + imax) // 2  # O(1)
            j = half_len - i  # O(1)

            if i < m and nums1[i] < nums2[j - 1]:
                # i is too small, must increase it
                imin = i + 1  # O(1)
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1 # O(1)
            else:
                # i is perfect
                if i == 0: 
                    max_of_left = nums2[j - 1] # O(1)
                elif j == 0: 
                    max_of_left = nums1[i - 1] # O(1)
                else: 
                    max_of_left = max(nums1[i - 1], nums2[j - 1]) # O(1)

                if (m + n) % 2 == 1:  # O(1)
                    return (max_of_left, 0)  # Only max_of_left is needed for odd total length

                if i == m: 
                    min_of_right = nums2[j] # O(1)
                elif j == n: 
                    min_of_right = nums1[i] # O(1)
                else: 
                    min_of_right = min(nums1[i], nums2[j]) # O(1)

                return (max_of_left, min_of_right) # O(1)

        raise ValueError("Input arrays are not sorted or have incorrect sizes.")

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    @staticmethod
    def create_linked_list(lst):
        dummy = ListNode()
        curr = dummy
        for data in lst:
            curr.next = ListNode(data)
            curr = curr.next
        return dummy.next

    @staticmethod
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.data)
            node = node.next
        return result

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
            * Each input will have exactly one solution. 
            * You may not use the same element twice.

        Constraints:
            * 2 <= nums.leng <= 10^4
            * -10^9 <= nums[i] <= 10^9
            * -10^9 <= target <= 10^9
        """
        
        # Algorithm type: Brute-force
        # Overall time complexity: O(n^2)
        # Overall space complexity: O(1)

        """
        for i in range(len(nums)):  # O(n)
            for j in range(i + 1, len(nums)):  # O(n)
                if nums[i] + nums[j] == target:  # O(1)
                    return [i, j]  # O(1)
        return []  # O(1)
        """

        # Algorithm type: Hash map
        # Overall time complexity: O(n)
        # Overall space complexity: O(n)

        # Initializing an empty dictionary
        num_to_index = {}  # O(1)

        # Iterating through the list n times
        for i, num in enumerate(nums):  # O(n)
            # Calculate the difference between the target and the current number
            complement = target - num  # O(1)

            # Check if dictionary contains the complement number
            if complement in num_to_index:  # O(1)
                # Access and return the indices
                return [num_to_index[complement], i]  # O(1)

            # Insert the current number and its index into the dictionary
            num_to_index[num] = i  # O(1)

        return []  # O(1)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        Assume the two numbers do not contain any leading zero, except the number zero itself.

        Args:
            l1 Optional[ListNode]: First linked list representing a number.
            l2 Optional[ListNode]: Second linked list representing a number.

        Returns:
            Optional[ListNode]: Linked list representing the sume of two numbers.
        
        Example:
            >>> solution = Solution()
            >>> solution.addTwoNumbers([2,4,3], [5,6,4])
            [7,0,8]
        
        Note:
            - The number of nodes in each linked list is in the range [1, 100]
            - 0 <= Node.val <= 9
            - It is guaranteed that the list represents a number that does not have leading zeros.
        """
        
        # Algorithm type: Two-pointer
        # Overall time complexity: O(max(n, m))
        # Overall space complexity: O(max(n, m))

        # Initialize a dummy node and a current pointer
        dummy = ListNode()  # O(1)
        tail = dummy  # O(1)

        # Initialize the carry variable
        carry = 0  # O(1)
        
        # Traverse both linked lists until both are exhausted and there is no carry left
        while l1 is not None or l2 is not None or carry != 0:  # O(max(m, n)), where m and n are the lengths of l1 and l2 respectively
            # Get the current values from both lists (or 0 if the list is exhausted)
            data1 = l1.data if l1 is not None else 0  # O(1)
            data2 = l2.data if l2 is not None else 0  # O(1)

            # Calculate the new digit and the carry
            sum = data1 + data2 + carry  # O(1)
            carry = sum // 10  # O(1)
            digit = sum % 10  # O(1)

            # Create a new node with the calculated digit and attach it to the result list
            tail.next = ListNode(digit)  # O(1)

            # Move the current pointer to the next node
            tail = tail.next  # O(1)
            
            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 is not None else None  # O(1)
            l2 = l2.next if l2 is not None else None  # O(1)

        # Return the next node of the dummy (the head of the resulting linked list)
        return dummy.next  # O(1)

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string `s`, find the length of the longest substring without repeating characters.

        Args:
            s: an input string

        Returns:
            int: The length of the longest substring without repeating characters.
        
        Example:
            >>> solution = Solution()
            >>> solution.lengthOfLongestSubstring("pwwkew")
            3
        
        Note:
            * `s` consists of English letters, digits, symbols and spaces.
        
        Constraints:
            * 0 <= s.length <= 5 * 10^4
        """
        
        # Algorithm type: Sliding window
        # Overall time complexity: O(n)
        # Overall space complexity: O(min(n, m))

        # Dictionary to store the last positions of each character
        char_map = {}  # O(1) space for each unique character
        
        # Left pointer of the sliding window
        left = 0  # O(1) initialization
        
        # Maximum length of substring found
        max_length = 0  # O(1) initialization

        # Iterate through the string with the right pointer of the sliding window
        for right in range(len(s)):  # O(n), where n is the length of the string
            # If the character is already in the map and its last position is within the current window
            if s[right] in char_map and char_map[s[right]] >= left:  # O(1) average case for dictionary lookup
                # Move the left pointer to the right of the last position of the character
                left = char_map[s[right]] + 1  # O(1) update

            # Update the last position of the character
            char_map[s[right]] = right  # O(1) update

            # Update the maximum length of the substring found
            max_length = max(max_length, right - left + 1)  # O(1) comparison and update

        # Return the maximum length of substring without repeating characters
        return max_length  # O(1)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, 
        return the `median` of the two sorted arrays.

        Args:
            nums1 List[int]: First list of numbers.
            nums2 List[int]: Second list of numbers.

        Returns:
            Optional[ListNode]: Reverse order sum of each input list node.
        
        Example:
            >>> solution = Solution()
            >>> solution.lengthOfLongestSubstring([1,2],[3,4])
            2.50000
        
        Note:
            * `s` consists of English letters, digits, symbols and spaces.
        
        Constraints:
            * nums1.length == m
            * nums2.length == n
            * 0 <= m <= 1000
            * 0 <= n <= 1000
            * 1 <= m + n <= 2000
            * -10^6 <= nums1[i], nums2[i] <= 10^6
            * Overall time complexity: O(log(m+n))
        """

        # Algorithm type: Binary-search
        # Overall time complexity: O(log(min(m,n)))
        # Overall space complexity: O(1)

        # if nums1 is empty
        if not nums1: # O(1)
            return (max(nums2)+min(nums2))/2 # O(1)
        
        # if nums2 is empty
        if not nums2: # O(1)
            return (max(nums1)+min(nums1))/2 # O(1)

        # if nums1 and nums2 are empty
        if not nums1 and not nums2:  # O(1)
            return None  # O(1)

        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2): # O(1)
            nums1, nums2 = nums2, nums1 # O(1)

        # Lengths of the two arrays
        m, n = len(nums1), len(nums2) # O(1)

        # Use the SearchAlgorithms class to find the correct partition
        max_of_left, min_of_right = SearchAlgorithms.binary_search_partition(nums1, nums2) # O(log(min(m,n)))    

        # If the total length is odd, return max_of_left
        if (m + n) % 2 == 1: # O(1)
            return max_of_left # O(1)

        # If the total length is even, return the average of max_of_left and min_of_right
        return (max_of_left + min_of_right) / 2.0 # O(1)

    def longestPalindrome(self, s: str) -> str:
        """
        Given a string `s`, return the longest palindromic substring in `s`.

        Args:
            s: input string of characters.

        Returns:
            str: longest palindromic substring in `s`.
        
        Example:
            >>> s = "babad"
            >>> solutions.longestPalindrome("babad")
            "bab"
               
        Constraints:
            * 1 <= s.length <= 1000
            * `s` consists of only digits and English letters.
        """

        # function to generate powerset of s
        def all_substrings_generator(s):
            length = len(s)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    yield s[i:j]


        # if all characters are the same
        if len(set(s)) == 1:
            return s
    
        # palindrome check
        for substring in all_substrings_generator(s):
            if substring == substring[::-1] and len(substring) > 1: # check to see if substring equals reverse substring
                pal = {substring: len(substring)}

        # if no palindromes exist
        if not pal: 
            return None
        else:
            return max(pal, key=pal.get) # return maximum length palindrome
        
