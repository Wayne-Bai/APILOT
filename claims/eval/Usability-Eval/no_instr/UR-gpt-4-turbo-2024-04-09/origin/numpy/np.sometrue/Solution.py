import numpy as np

# Example array
arr = np.array([[0, 1, 0], [0, 0, 0]])

# Test whether any element along an axis evaluates to True
result = np.any(arr, axis=0)

print(result)
