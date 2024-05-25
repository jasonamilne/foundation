from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_length_of_empty_string(solution):
    """Test with an empty string."""
    assert solution.longestPalindrome("") == None

def test_length_of_empty_string(solution):
    """Test with an empty string."""
    assert solution.longestPalindrome("a") == "a"

def test_length_of_2_string(solution):
    """Test with an empty string."""
    assert solution.longestPalindrome("bb") == "bb"

def test_length_of_3_string(solution):
    """Test with an empty string."""
    assert solution.longestPalindrome("cac") == "cac"

def test_length_of_cap_string(solution):
    """Test with an empty string."""
    assert solution.longestPalindrome("BABAD") == "ABA" or solution.longestPalindrome("BABAD") == "BAB"
