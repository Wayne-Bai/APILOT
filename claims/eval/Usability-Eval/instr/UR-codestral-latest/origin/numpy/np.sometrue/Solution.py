import numpy as np

# Creating a numpy array for testing
arr = np.array([[False, True, False],
               [True, False, False],
               [False, False, False]])

# Checking if any array element along the given axis evaluates to True
# Here, we're checking along axis 0 (rows)
any_true_along_axis_0 = np.any(arr, axis=0)
print("Any True along axis 0:", any_true_along_axis_0)

# Checking along axis 1 (columns)
any_true_along_axis_1 = np.any(arr, axis=1)
print("Any True along axis 1:", any_true_along_axis_1)
