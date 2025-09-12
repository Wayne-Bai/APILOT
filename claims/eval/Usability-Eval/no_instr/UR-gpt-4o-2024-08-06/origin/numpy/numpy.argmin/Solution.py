import numpy as np

# Sample 2D array
array = np.array([[4, 2, 7], [9, 1, 5], [3, 8, 6]])

# Get the indices of the minimum values along axis 0 (column-wise)
min_indices_col = np.argmin(array, axis=0)

# Get the indices of the minimum values along axis 1 (row-wise)
min_indices_row = np.argmin(array, axis=1)

print("Indices of the minimum values along axis 0:", min_indices_col)
print("Indices of the minimum values along axis 1:", min_indices_row)
