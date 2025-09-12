import numpy as np

# Create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Use prod function to return the product of array elements over a given axis
# Axis 0 means the product will be computed vertically (row-wise)
prod_axis_0 = np.prod(arr, axis=0)
print("Product over axis 0: ", prod_axis_0)

# Axis 1 means the product will be computed horizontally (column-wise)
prod_axis_1 = np.prod(arr, axis=1)
print("Product over axis 1: ", prod_axis_1)

# Without specifying axis, the product will be computed for the entire array
prod_entire_array = np.prod(arr)
print("Product of the entire array: ", prod_entire_array)
