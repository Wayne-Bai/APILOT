import numpy as np

# Create a 2D numpy array
arr = np.array([[5, 2, 8], [6, 3, 1]])

# Use np.argmin to get the indices of the minimum values along the 0th axis (rows)
print(np.argmin(arr, axis=0))

# Use np.argmin to get the indices of the minimum values along the 1st axis (columns)
print(np.argmin(arr, axis=1))
