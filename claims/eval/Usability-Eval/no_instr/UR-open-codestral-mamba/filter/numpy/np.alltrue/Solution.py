import numpy as np

# Create a sample array
arr = np.array([[1, 1], [2, 2]])

# Test if all elements in the array are non-zero along a given axis
result = np.all(arr)

print(result)
