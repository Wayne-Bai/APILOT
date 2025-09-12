import numpy as np

# Create a sample array
arr = np.array([[True, False, True], [True, True, False]])

# Test whether all array elements along axis 0 evaluate to True
result = np.all(arr, axis=0)
print(result)
