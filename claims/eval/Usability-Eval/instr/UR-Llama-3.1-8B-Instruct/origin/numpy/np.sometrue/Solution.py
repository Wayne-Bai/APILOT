import numpy as np

# Creating a sample numpy array
arr = np.array([[True, True, False], [True, False, True]])

# Test whether any array element along a given axis evaluates to True
# Using np.any() function along the 0th axis (rows)
print("Any element is True in a row:", np.any(arr, axis=0))

# Using np.any() function along the 1st axis (columns)
print("Any element is True in a column:", np.any(arr, axis=1))
