import numpy as np

# Create a numpy array with some values
array = np.array([1, 2, 0, 3, 0, 4])

# Use np.any to check if any element in the array is True
print(np.any(array))  # Output: True

# Use np.any along a given axis. For 2D array
array_2d = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 0]])

# Axis 0 is for columns and Axis 1 is for rows
print(np.any(array_2d, axis=0))  # Output: [ True  True  True]
print(np.any(array_2d, axis=1))  # Output: [ True  True  True]

# Resource from:
# https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any
