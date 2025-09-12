import numpy as np

# Sample array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the indices of the maximum values along axis 1 (columns)
max_indices = np.argmax(arr, axis=1)

print("Indices of the maximum values along axis 1:", max_indices)
