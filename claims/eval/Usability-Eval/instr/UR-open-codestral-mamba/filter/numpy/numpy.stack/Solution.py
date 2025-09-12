import numpy as np

# Arrays to be joined
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Join along a new axis
joined_array = np.stack((array1, array2), axis=0)

print(joined_array)
