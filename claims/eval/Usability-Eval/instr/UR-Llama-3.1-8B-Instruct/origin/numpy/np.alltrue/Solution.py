import numpy as np

# Create a numpy array with some boolean values
arr = np.array([[True, False, True], [True, True, False]])

# Test along axis 0 (default axis)
print(" Along axis 0 (default axis):", np.all(arr, axis=0))

# Test along axis 1
print(" Along axis 1:", np.all(arr, axis=1))

# Test along axis 0 and 1 (axis None or -1 means all axes)
print(" Along all axes:", np.all(arr, axis=None))
