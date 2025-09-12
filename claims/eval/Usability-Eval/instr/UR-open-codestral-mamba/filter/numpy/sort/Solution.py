import numpy as np

# Original unsorted array
arr = np.array([9, 5, 1, 8, 3])

# Using numpy's sort function to get sorted copy
sorted_arr = np.sort(arr)

print(f"Original Array: {arr}")
print(f"Sorted Array: {sorted_arr}")
