from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_positive(solution):
    assert solution.find_max([1,2,3,4,5]) == 5

def test_negative(solution):
    assert solution.find_max([-1,-2,-3,-4,-5]) == -1

def test_negative_positive(solution):
    assert solution.find_max([-2,-1,0,+1,+2]) == 2

def test_same(solution):
    assert solution.find_max([0,0,0,0,0]) == 0

def test_empty(solution):
    assert solution.find_max([]) == None

def test_single(solution):
    assert solution.find_max([10]) == 10

def test_same_positive(solution):
    assert solution.find_max([7,7,7,7,7,7]) == 7

def test_large_positive(solution):
    assert solution.find_max([1000000, 2000000, 3000000]) == 3000000

def test_large_negative(solution):
    assert solution.find_max([-1000000, -2000000, -3000000]) == -1000000

def test_large_mixed_large_small(solution):
    assert solution.find_max([-1000000, 1000000, -0.00001, 0, 0.00001, 999999, -999999]) == 1000000

def test_floats(solution):
    assert solution.find_max([1.5,2.5,-3.5,0.5]) == 2.5

def test_duplicates(solution):
    assert solution.find_max([1,2,2,3,1,-1,-2,-3,3]) == 3

def test_reversed_sorted_list(solution):
    assert solution.find_max([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9

def test_long_list(solution):
    long_list = list(range(-100000, 100000))  # A list with 200,000 elements
    assert solution.find_max(long_list) == 99999
