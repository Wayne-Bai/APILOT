import numpy as np

# Creating a 2D array
array = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

# Checking if any element along a given axis (e.g., axis=0) evaluates to True
result = np.any(array, axis=0)

print(result)
