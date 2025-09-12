import numpy as np

# Assuming you have two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack arrays in sequence horizontally (column wise)
stacked_array = np.hstack((arr1, arr2))

print(stacked_array)
