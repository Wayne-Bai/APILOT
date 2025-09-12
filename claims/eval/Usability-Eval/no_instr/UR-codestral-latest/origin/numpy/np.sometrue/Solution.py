import numpy as np

# Define the numpy array
arr = np.array([[False, True, False], [False, False, False], [True, False, True]])

# Use numpy's any() function to test whether any array element along a given axis evaluates to True.
result = np.any(arr, axis=1)

print(result)
