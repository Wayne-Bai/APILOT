import numpy as np

# Creating example arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Joining arrays along a new axis (axis=0)
joined_array = np.stack((array1, array2), axis=0)

print(joined_array)
