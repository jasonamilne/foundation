from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_myAoi(solution):

    # Normal cases
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("    -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -2147483648  # INT_MIN overflow
    assert solution.myAtoi("91283472332") == 2147483647  # INT_MAX overflow
    assert solution.myAtoi("123") == 123
    assert solution.myAtoi("+123") == 123
    assert solution.myAtoi("-123") == -123

    # Edge cases
    assert solution.myAtoi("") == 0
    assert solution.myAtoi("     ") == 0
    assert solution.myAtoi("+") == 0
    assert solution.myAtoi("-") == 0
    assert solution.myAtoi("+-2") == 0
    assert solution.myAtoi("-+2") == 0
    assert solution.myAtoi("00000-42a1234") == 0
    assert solution.myAtoi("00000123") == 123

    # Test cases with non-digit characters
    assert solution.myAtoi("abc123") == 0
    assert solution.myAtoi("123abc") == 123
    assert solution.myAtoi("0") == 0
    assert solution.myAtoi("-0") == 0

    # Test cases with maximum and minimum values
    assert solution.myAtoi(str(2**31 - 1)) == 2147483647
    assert solution.myAtoi(str(-2**31)) == -2147483648
    assert solution.myAtoi(str(2**31)) == 2147483647
    assert solution.myAtoi(str(-2**31 - 1)) == -2147483648

    # Test cases with long strings
    assert solution.myAtoi(" " * 1000 + "12345") == 12345
    assert solution.myAtoi(" " * 1000 + "-12345") == -12345
