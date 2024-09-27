import time
from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

# Pytest Benchmark for small input
def test_benchmark_small_input(solution,benchmark):
    small_list = list(range(1000))  # Small input size
    benchmark(solution.find_max, small_list)

# Pytest Benchmark for medium input
def test_benchmark_medium_input(solution,benchmark):
    medium_list = list(range(100000))  # Medium input size
    benchmark(solution.find_max, medium_list)

# Pytest Benchmark for large input
def test_benchmark_large_input(solution,benchmark):
    large_list = list(range(10000000))  # Large input size
    benchmark(solution.find_max, large_list)
