import numpy as np

# Assuming 'arr' is your numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# To find the indices of the minimum values along the axis 0 (rows)
min_indices_rows = np.argmin(arr, axis=0)

# To find the indices of the minimum values along the axis 1 (columns)
min_indices_cols = np.argmin(arr, axis=1)

print("Indices of minimum values along rows:", min_indices_rows)
print("Indices of minimum values along columns:", min_indices_cols)
