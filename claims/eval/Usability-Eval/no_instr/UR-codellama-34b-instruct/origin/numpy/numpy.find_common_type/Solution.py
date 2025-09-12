import numpy as np

# Define two arrays with different dtypes
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([4, 5, 6], dtype=np.int32)

# Determine the common type of the two arrays
common_type = np.promote_types(arr1.dtype, arr2.dtype)
print("Common type:", common_type)
