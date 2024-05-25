from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_isPalindrome(solution):
    # Test cases based on the provided examples
    assert solution.isPalindrome(121) == True, "Test case 1 failed"
    assert solution.isPalindrome(-121) == False, "Test case 2 failed"
    assert solution.isPalindrome(10) == False, "Test case 3 failed"

    # Additional test cases
    assert solution.isPalindrome(0) == True, "Test case 4 failed"  # Edge case: single digit, 0
    assert solution.isPalindrome(1) == True, "Test case 5 failed"  # Edge case: single digit, 1
    assert solution.isPalindrome(12321) == True, "Test case 6 failed"  # Odd number of digits
    assert solution.isPalindrome(1221) == True, "Test case 7 failed"  # Even number of digits
    assert solution.isPalindrome(123) == False, "Test case 8 failed"  # Not a palindrome
    assert solution.isPalindrome(-101) == False, "Test case 9 failed"  # Negative number
    assert solution.isPalindrome(1001) == True, "Test case 10 failed"  # Palindrome with zeros
    assert solution.isPalindrome(1000021) == False, "Test case 11 failed"  # Large number, not a palindrome
    assert solution.isPalindrome(1234321) == True, "Test case 12 failed"  # Large palindrome

    # Testing the boundaries
    assert solution.isPalindrome(2**31 - 1) == False, "Test case 13 failed"  # Upper boundary (not a palindrome)
    assert solution.isPalindrome(-2**31) == False, "Test case 14 failed"  # Lower boundary (not a palindrome)
