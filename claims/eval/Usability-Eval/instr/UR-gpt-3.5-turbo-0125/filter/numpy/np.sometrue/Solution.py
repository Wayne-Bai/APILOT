
import numpy as np

# Create an array
arr = np.array([[False, False, False],
                [False, True, False],
                [False, False, False]])

# Test whether any element along axis=1 evaluates to True
result = np.any(arr, axis=1)

print(result)
