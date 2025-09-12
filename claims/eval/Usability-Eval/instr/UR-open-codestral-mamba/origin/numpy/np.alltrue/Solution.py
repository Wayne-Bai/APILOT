import numpy as np

# Create numpy array with bool values
arr = np.array([[True, False], [True, True]])

# Testing all elements along axis 0
print(np.all(arr, axis=0))

# Testing all elements along axis 1
print(np.all(arr, axis=1))
