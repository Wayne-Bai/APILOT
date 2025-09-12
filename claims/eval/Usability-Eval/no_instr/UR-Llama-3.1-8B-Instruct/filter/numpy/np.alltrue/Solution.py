import numpy as np

# Create a sample array
arr = np.array([[True, True, False], [True, True, True]])

print(np.all(arr, axis=0))  # All elements along a particular axis
print(np.all(arr, axis=1))  # All elements along a particular axis
