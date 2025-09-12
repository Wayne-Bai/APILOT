import numpy as np

# Define two arrays with different data types
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)

# Determine the common type for these arrays following standard coercion rules
common_type = np.common_type(array1, array2)

print("Common type:", common_type)
