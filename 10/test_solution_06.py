from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example1_string(solution):
    assert solution.convert(s = "PAYPALISHIRING", numRows = 3) == "PAHNAPLSIIGYIR"

def test_example2_string(solution):
    assert solution.convert(s = "PAYPALISHIRING", numRows = 4) == "PINALSIGYAHRPI"

def test_example3_string(solution):
    assert solution.convert(s = "A", numRows = 1) == "A"
