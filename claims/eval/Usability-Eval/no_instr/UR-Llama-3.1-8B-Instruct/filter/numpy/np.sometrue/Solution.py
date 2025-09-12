import numpy as np

# Define a 2D numpy array
arr = np.array([[True, False, True], [False, True, False]])

# Define the axis along which to check
axis = 0

# Use np.any along the given axis to check if any element evaluates to True
result = np.any(arr, axis=axis)

print(result)  # Output: [ True  True]
