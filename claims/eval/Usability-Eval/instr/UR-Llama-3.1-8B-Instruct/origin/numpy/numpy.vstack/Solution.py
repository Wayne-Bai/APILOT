# Import the numpy library
import numpy as np

# Define two 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Stack the arrays vertically (row wise)
stacked_arr = np.vstack((arr1, arr2))

# Print the stacked array
print(stacked_arr)
