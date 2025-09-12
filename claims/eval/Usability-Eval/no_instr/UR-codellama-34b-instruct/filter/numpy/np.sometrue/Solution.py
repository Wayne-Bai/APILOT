import numpy as np

# Create a sample array
arr = np.array([[True, False], [False, True]])

# Test if any element along the first axis (row) is true
result = np.any(arr, axis=0)
print(result)  # Output: [ True  False]

# Test if any element along the second axis (column) is true
result = np.any(arr, axis=1)
print(result)  # Output: [False  True]
