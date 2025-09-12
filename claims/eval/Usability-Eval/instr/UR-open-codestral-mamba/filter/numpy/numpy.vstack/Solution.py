import numpy as np

# Creating two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Using np.vstack() to stack arrays in sequence vertically (row wise)
stacked_array = np.vstack((array1, array2))

print(stacked_array)
