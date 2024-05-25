from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_length_of_longest_substring_empty_string(solution):
    """Test with an empty string."""
    assert solution.lengthOfLongestSubstring("") == 0

def test_length_of_longest_substring_single_char(solution):
    """Test with a single character."""
    assert solution.lengthOfLongestSubstring("a") == 1

def test_length_of_longest_substring_all_unique(solution):
    """Test with all unique characters."""
    assert solution.lengthOfLongestSubstring("abcde") == 5

def test_length_of_longest_substring_repeating_chars(solution):
    """Test with all repeating characters."""
    assert solution.lengthOfLongestSubstring("aaaaa") == 1

def test_length_of_longest_substring_mixed_chars(solution):
    """Test with mixed unique and repeating characters."""
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3

def test_length_of_longest_substring_with_spaces(solution):
    """Test with spaces included."""
    assert solution.lengthOfLongestSubstring("p ww k ew") == 4

def test_length_of_longest_substring_with_symbols(solution):
    """Test with special symbols."""
    assert solution.lengthOfLongestSubstring("a!b@c#d$") == 8

def test_length_of_longest_substring_with_numbers(solution):
    """Test with numbers included."""
    assert solution.lengthOfLongestSubstring("123123456") == 6

def test_length_of_longest_substring_combined_case(solution):
    """Test with a combined case."""
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
