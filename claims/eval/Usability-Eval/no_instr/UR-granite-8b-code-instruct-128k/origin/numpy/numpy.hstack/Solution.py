import numpy as np

# Create two arrays to stack
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Stack the arrays horizontally
stacked_arr = np.hstack((arr1, arr2))

# Print the result
print(stacked_arr)
