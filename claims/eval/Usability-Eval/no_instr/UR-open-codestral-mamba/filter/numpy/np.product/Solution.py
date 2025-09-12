import numpy as np

# Create a numpy array
arr = np.array([[1, 2], [3, 4]])

# Using the 'np.prod' function to return the product of array elements over a given axis
# axis = None returns the complete product of all elements
result_all = np.prod(arr)

# axis = 0 returns the product along the first column for each row
result_column = np.prod(arr, axis=0)

# axis = 1 returns the product inside each row
result_row = np.prod(arr, axis=1)

result_all, result_column, result_row
