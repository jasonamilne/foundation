import time
from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_time_small_input(solution):
    small_list = list(range(1000))  # Small input size
    start_time = time.time()
    solution.find_max(small_list)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken for small input: {execution_time} seconds")
    assert execution_time < 0.1  # Ensure it finishes in less than 100ms

def test_time_medium_input(solution):
    medium_list = list(range(100000))  # Medium input size
    start_time = time.time()
    solution.find_max(medium_list)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken for medium input: {execution_time} seconds")
    assert execution_time < 0.5  # Ensure it finishes in less than 500ms

def test_time_large_input(solution):
    large_list = list(range(10000000))  # Large input size
    start_time = time.time()
    solution.find_max(large_list)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken for large input: {execution_time} seconds")
    assert execution_time < 1.0  # Ensure it finishes in less than 1 second
