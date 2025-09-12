
import numpy as np

# Create a sample 2D array
arr = np.array([[1, 0, 1], [0, 1, 0]])

# Test whether all elements along axis=0 (first dimension) are True
result = np.all(arr, axis=0)
print(result)  # Output: [False False]

# Test whether all elements along axis=1 (second dimension) are True
result = np.all(arr, axis=1)
print(result)  # Output: [True False]
