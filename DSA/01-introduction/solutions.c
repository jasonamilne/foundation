#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

int find_max(int *nums, int size) {
    if (size == 0) {
        return INT_MIN;  // Return INT_MIN if array is empty
    }

    int max_num = nums[0];  // Initialize with the first element

    for (int i = 1; i < size; i++) {
        if (nums[i] > max_num) {
            max_num = nums[i];
        }
    }

    return max_num;
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

    clock_t start = clock();
    int max_value = find_max(nums, size);
    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Max Value: %d\n", max_value);
    printf("Time taken: %f seconds\n", time_taken);

    // Free the allocated memory
    free(nums);

    return 0;
}
