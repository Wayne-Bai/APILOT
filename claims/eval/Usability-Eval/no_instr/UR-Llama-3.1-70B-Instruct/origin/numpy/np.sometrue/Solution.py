import numpy as np

# Create a numpy array
arr = np.array([[True, False], [False, True]])

# Test whether any array element along axis=0 (columns) evaluates to True
print(np.any(arr, axis=0))

# Test whether any array element along axis=1 (rows) evaluates to True
print(np.any(arr, axis=1))

# Test whether any array element evaluates to True (no specific axis)
print(np.any(arr))
