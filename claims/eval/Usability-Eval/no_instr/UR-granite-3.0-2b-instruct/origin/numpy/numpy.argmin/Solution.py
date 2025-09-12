import numpy as np

# Sample data
data = np.array([[4, 2, 9, 7], [1, 5, 3, 6], [8, 3, 2, 1]])

# Find the indices of the minimum values along axis 0 (rows)
row_min_indices = np.argmin(data, axis=0)

# Find the indices of the minimum values along axis 1 (columns)
col_min_indices = np.argmin(data, axis=1)

print("Row minimum indices:", row_min_indices)
print("Column minimum indices:", col_min_indices)
