import numpy as np

# Define a 2D array
arr = np.array([[3, 4, 5], [6, 7, 8], [9, 1, 2]])

# Find the indices of the minimum values along an axis
min_index = np.unravel_index(arr.argmin(), arr.shape)

print("Indices of the minimum values along an axis:", min_index)
