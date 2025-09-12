import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Use the `argmax` function to find the indices of the maximum values along an axis
# The '0' argument indicates that the maximum should be found along axis 0 (i.e., columns)
column_indices = np.argmax(arr, axis=0)
print("Column indices:", column_indices)

# The '1' argument indicates that the maximum should be found along axis 1 (i.e., rows)
row_indices = np.argmax(arr, axis=1)
print("Row indices:", row_indices)
