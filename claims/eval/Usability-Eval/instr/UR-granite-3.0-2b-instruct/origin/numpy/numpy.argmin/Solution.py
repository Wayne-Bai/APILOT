import numpy as np

# Sample data
data = np.array([[4, 2, 9], [7, 5, 6], [3, 8, 1]])

# Find the indices of the minimum values along axis 0 (rows)
row_indices = np.argwhere(data == data.min(axis=0))

# Find the indices of the minimum values along axis 1 (columns)
col_indices = np.argwhere(data == data.min(axis=1))

print("Row indices:", row_indices)
print("Column indices:", col_indices)
