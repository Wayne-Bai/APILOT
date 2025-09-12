
import numpy as np

# create a sample array for demonstration purposes
arr = np.array([[1, 2, 3], [4, 5, 6]])

# use argmin to find the indices of the minimum values along the first axis (rows)
row_indices = arr.argmin(axis=0)

# use argmin to find the indices of the minimum values along the second axis (columns)
col_indices = arr.argmin(axis=1)

print("Row indices:", row_indices)
print("Column indices:", col_indices)
