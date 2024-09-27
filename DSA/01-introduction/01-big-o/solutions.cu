#include <stdio.h>
#include <limits.h>
#include <cuda_runtime.h>

__global__ void max_reduction(int *data, int *result, int n) {
    extern __shared__ int sdata[];  // Shared memory for partial results
    int tid = threadIdx.x;
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    // Load elements into shared memory
    if (i < n) {
        sdata[tid] = data[i];
    } else {
        sdata[tid] = INT_MIN;  // If out of bounds, set to the minimum value
    }
    __syncthreads();

    // Reduce in shared memory
    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] = max(sdata[tid], sdata[tid + s]);
        }
        __syncthreads();
    }

    // Write result for this block
    if (tid == 0) result[blockIdx.x] = sdata[0];
}

int find_max_cuda(int *h_data, int n) {
    int *d_data, *d_result, *h_result;
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    h_result = (int*) malloc(blocksPerGrid * sizeof(int));
    cudaMalloc(&d_data, n * sizeof(int));
    cudaMalloc(&d_result, blocksPerGrid * sizeof(int));

    cudaMemcpy(d_data, h_data, n * sizeof(int), cudaMemcpyHostToDevice);

    // Launch kernel
    max_reduction<<<blocksPerGrid, threadsPerBlock, threadsPerBlock * sizeof(int)>>>(d_data, d_result, n);

    // Copy result back to host
    cudaMemcpy(h_result, d_result, blocksPerGrid * sizeof(int), cudaMemcpyDeviceToHost);

    // Final reduction on the CPU
    int max_value = h_result[0];
    for (int i = 1; i < blocksPerGrid; i++) {
        if (h_result[i] > max_value) {
            max_value = h_result[i];
        }
    }

    cudaFree(d_data);
    cudaFree(d_result);
    free(h_result);

    return max_value;
}

int main(int argc, char *argv[]) {
    int size = 1000;  // Default size, can be modified based on input
    if (argc > 1) {
        sscanf(argv[1], "%d", &size);  // Get size from command-line argument
    }

    // Dynamically allocate memory for the array to handle large input sizes
    int *nums = (int *)malloc(size * sizeof(int));
    if (nums == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Fill array with values 0, 1, 2, ..., size-1
    for (int i = 0; i < size; i++) {
        nums[i] = i;
    }

    // Find max using CUDA
    int max_value = find_max_cuda(nums, size);

    printf("Max Value: %d\n", max_value);

    // Free the allocated memory
    free(nums);

    return 0;
}
