import numpy as np

# Sample arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# Stack arrays vertically
stacked_array = np.concatenate((arr1, arr2, arr3), axis=0)

print(stacked_array)
