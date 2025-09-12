import numpy as np

# Assuming you have two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack arrays in sequence vertically (row wise)
stacked_array = np.vstack((arr1, arr2))

print(stacked_array)
