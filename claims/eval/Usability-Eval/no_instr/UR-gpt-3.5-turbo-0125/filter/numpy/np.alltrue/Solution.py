
import numpy as np

# Create a sample numpy array
arr = np.array([[True, True, True],
                [False, True, True],
                [True, True, True]])

# Test whether all array elements along axis=1 evaluate to True
result = np.all(arr, axis=1)

print(result)
