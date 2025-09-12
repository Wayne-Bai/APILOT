import numpy as np

# Create a sample array
arr = np.array([True, False, True, True])

# Test if all elements along a given axis evaluate to True
result = np.all(arr)

print(result)
