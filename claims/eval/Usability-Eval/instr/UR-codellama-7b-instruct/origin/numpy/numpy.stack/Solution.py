import numpy as np

# Create a sequence of arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 10], [11, 12]])

# Join the arrays along a new axis (axis=0)
joined_arr = np.stack((arr1, arr2, arr3), axis=0)

print(joined_arr)
