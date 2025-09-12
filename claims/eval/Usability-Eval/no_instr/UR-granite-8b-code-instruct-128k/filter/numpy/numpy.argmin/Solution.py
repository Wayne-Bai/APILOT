import numpy as np
# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Find the indices of the minimum values along the first axis
indices = np.argmin(arr, axis=0)
print(indices)
