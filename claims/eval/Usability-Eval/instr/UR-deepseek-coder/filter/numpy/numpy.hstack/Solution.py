import numpy as np

# Example arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Stack arrays horizontally
stacked_array = np.concatenate((array1[:, np.newaxis], array2[:, np.newaxis]), axis=1)

print(stacked_array)
