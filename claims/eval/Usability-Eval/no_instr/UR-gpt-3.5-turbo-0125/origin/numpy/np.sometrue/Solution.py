
import numpy as np

# Create a sample array
arr = np.array([[False, False, False],
                [False, True, False],
                [False, False, False]])

# Test whether any array element along a given axis evaluates to True
result = np.any(arr, axis=1)

print(result)
