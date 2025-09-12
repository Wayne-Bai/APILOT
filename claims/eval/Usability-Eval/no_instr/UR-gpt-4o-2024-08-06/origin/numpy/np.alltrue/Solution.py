import numpy as np

# Create a sample 2D array
array = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

# Test whether all elements along a given axis evaluate to True
# Using the axis=0 to check column-wise
result_axis_0 = np.all(array, axis=0)
print("All elements along axis 0 are True:", result_axis_0)

# Using the axis=1 to check row-wise
result_axis_1 = np.all(array, axis=1)
print("All elements along axis 1 are True:", result_axis_1)
