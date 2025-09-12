import numpy as np

# Example arrays
array_1 = np.array([[1, 2], [3, 4]])
array_2 = np.array([[5, 6], [7, 8]])

# Join along a new axis (axis=0)
joined_array = np.concatenate((array_1, array_2), axis=0)
print(joined_array)
