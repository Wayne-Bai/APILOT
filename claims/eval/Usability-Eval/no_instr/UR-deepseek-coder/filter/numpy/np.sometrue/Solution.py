import numpy as np

# Example array
arr = np.array([[0, 1, 2], [3, 4, 5]])

# Test whether any element along the specified axis evaluates to True
result = np.any(arr, axis=0)

print(result)
