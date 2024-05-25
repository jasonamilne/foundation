from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_isMatch(solution):
    # Basic test cases from the prompt
    assert solution.isMatch("aa", "a") == False, "Test case 1 failed"
    assert solution.isMatch("aa", "a*") == True, "Test case 2 failed"
    assert solution.isMatch("ab", ".*") == True, "Test case 3 failed"
    assert solution.isMatch("aab", "c*a*b") == True, "Test case 4 failed"
    assert solution.isMatch("mississippi", "mis*is*p*.") == False, "Test case 5 failed"

    # Additional test cases for edge scenarios and varying patterns
    assert solution.isMatch("", "") == True, "Test case 6 failed"  # Both empty
    assert solution.isMatch("a", "") == False, "Test case 7 failed"  # Non-empty string, empty pattern
    assert solution.isMatch("", ".*") == True, "Test case 8 failed"  # Empty string, pattern that can match anything zero times
    assert solution.isMatch("abcd", "d*") == False, "Test case 9 failed"  # Pattern does not match the string at all
    assert solution.isMatch("abcd", ".*d") == True, "Test case 10 failed"  # Pattern matches any characters followed by 'd'
    assert solution.isMatch("abcd", ".*c") == False, "Test case 11 failed"  # Pattern matches any characters followed by 'c'
    assert solution.isMatch("aaa", "a*a") == True, "Test case 12 failed"  # Pattern matches multiple 'a's followed by 'a'
    assert solution.isMatch("aaa", "ab*a*c*a") == True, "Test case 13 failed"  # Complex pattern with multiple star operations
    assert solution.isMatch("a", "ab*") == True, "Test case 14 failed"  # 'a' followed by zero or more 'b's
    assert solution.isMatch("ab", ".*c") == False, "Test case 15 failed"  # Pattern should end with 'c'
    assert solution.isMatch("aaa", "a*a") == True, "Test case 16 failed"  # Pattern matches multiple 'a's followed by 'a'

    # Cases with multiple stars and dots
    assert solution.isMatch("aaa", ".*") == True, "Test case 17 failed"  # Pattern matches zero or more of any character
    assert solution.isMatch("ab", ".*..") == True, "Test case 18 failed"  # Pattern too long to match string
    assert solution.isMatch("ab", ".*c") == False, "Test case 19 failed"  # Pattern expects 'c' at the end

    # Edge case with zero characters and stars
    assert solution.isMatch("abc", "a*b*c*") == True, "Test case 20 failed"  # Each character can be matched zero or more times
