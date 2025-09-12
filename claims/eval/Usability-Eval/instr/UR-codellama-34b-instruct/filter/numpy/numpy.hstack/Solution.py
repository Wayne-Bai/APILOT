import numpy as np

# Create some sample arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack the arrays horizontally (column-wise) using np.stack()
stacked_arr = np.stack((arr1, arr2), axis=1)

print(stacked_arr)
