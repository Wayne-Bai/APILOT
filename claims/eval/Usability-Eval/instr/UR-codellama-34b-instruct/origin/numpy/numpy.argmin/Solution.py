import numpy as np

# Define the array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Find the indices of the minimum values along the first axis (rows)
min_indices = np.argmin(arr, axis=0)
print("Indices of minimum values along rows:", min_indices)

# Find the indices of the minimum values along the second axis (columns)
min_indices = np.argmin(arr, axis=1)
print("Indices of minimum values along columns:", min_indices)
