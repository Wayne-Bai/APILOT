import numpy as np

# Create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the axis along which to test
axis = 1

# Use numpy's any function along the specified axis
result = np.any(arr, axis=axis)

print(result)
