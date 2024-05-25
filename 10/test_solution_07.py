from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example1_string(solution):
    assert solution.reverse(x = 123) == 321

def test_example2_string(solution):
    assert solution.reverse(x = -123) == -321

def test_example3_string(solution):
    assert solution.reverse(x = 120) == 21
