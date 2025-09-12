import numpy as np

# Create a numpy array
arr = np.array([[True, False, True], [False, True, False]])

# Use the all() function along the specified axis
# axis=0 checks along the columns, axis=1 checks along the rows
print("All elements along axis 0:", np.all(arr, axis=0))
print("All elements along axis 1:", np.all(arr, axis=1))

# Create another array with all True values
arr_true = np.array([[True, True, True], [True, True, True]])

# Test all elements along the specified axis
print("All elements along axis 0 in arr_true:", np.all(arr_true, axis=0))
print("All elements along axis 1 in arr_true:", np.all(arr_true, axis=1))
