import numpy as np

# Create two 2D arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stack arrays vertically (row wise)
stacked_arr = np.vstack((arr1, arr2))

print(stacked_arr)
