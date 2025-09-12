import numpy as np

# Here's an example where we'll create three 1D arrays and stack them

# Creating three 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# Stack the arrays along a new axis
stacked_array = np.stack((arr1, arr2, arr3), axis=1)

print(stacked_array)
