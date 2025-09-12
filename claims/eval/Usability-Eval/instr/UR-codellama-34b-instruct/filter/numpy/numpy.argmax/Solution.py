
import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the indices of the maximum values along the first axis (rows)
max_indices = np.argmax(arr, axis=0)

print(max_indices)  # Output: array([2, 1, 0])
