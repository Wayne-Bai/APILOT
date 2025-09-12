import numpy as np

# Example 1D array
array_1d = np.array([1, 2, 3, 4, 5])

# Calculate the product along axis=0 (default axis)
result_1d = np.prod(array_1d)
print(result_1d)

# Example 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate the product along axis=0
result_axis0 = np.prod(array_2d, axis=0)
print(result_axis0)

# Calculate the product along axis=1
result_axis1 = np.prod(array_2d, axis=1)
print(result_axis1)
