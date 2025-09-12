import numpy as np

# Create a sample numpy array
arr = np.array([True, False, True, False, True])

# Test whether any array element along a given axis evaluates to True
result = np.any(arr)

print(result)
