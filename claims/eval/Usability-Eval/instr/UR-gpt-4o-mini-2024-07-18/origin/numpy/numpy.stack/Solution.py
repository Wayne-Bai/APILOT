import numpy as np

# Create sample arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Join arrays along a new axis (axis=0 for vertical stacking, axis=1 for horizontal stacking)
joined_array = np.concatenate((array1[:, np.newaxis], array2[:, np.newaxis]), axis=1)

print(joined_array)
