import numpy as np

# Sample arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# Join the arrays along a new axis
joined_array = np.concatenate((arr1[:, np.newaxis], arr2[:, np.newaxis], arr3[:, np.newaxis]), axis=1)

print(joined_array)
