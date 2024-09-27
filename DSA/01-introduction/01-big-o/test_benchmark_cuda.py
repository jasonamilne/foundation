import subprocess
import pytest

# Helper function to run the CUDA program with in-memory data
def run_cuda_program(input_size):
    # Call the CUDA program with the input size as a command-line argument
    result = subprocess.run(['./solutions', str(input_size)], stdout=subprocess.PIPE)
    
    # Capture the output and split the lines
    output_lines = result.stdout.decode('utf-8').strip().split('\n')
    
    # The first line should contain the max value, so return only that
    max_value = int(output_lines[0].split(': ')[1])  # Extract the integer value from "Max Value: X"
    return max_value

@pytest.mark.benchmark
def test_benchmark_cuda_small_input(benchmark):
    benchmark(run_cuda_program, 1000)  # Small input (1,000 elements)

@pytest.mark.benchmark
def test_benchmark_cuda_medium_input(benchmark):
    benchmark(run_cuda_program, 100000)  # Medium input (100,000 elements)

@pytest.mark.benchmark
def test_benchmark_cuda_large_input(benchmark):
    benchmark(run_cuda_program, 10000000)  # Large input (10,000,000 elements)
