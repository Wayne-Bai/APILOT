import numpy as np

# Create a 2D numpy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use numpy's argmax() function to find the indices of the maximum values along an axis
max_indices = np.argmax(array_2d, axis=1)

print("Indices of maximum values along axis 1: ", max_indices)
