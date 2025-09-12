import numpy as np

# Define example arrays with different data types
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
array3 = np.array([1+1j, 2+2j], dtype=np.complex128)

# Find common data type following standard coercion rules
result_dtype = np.find_common_type([array1.dtype, array2.dtype, array3.dtype], [])

print("The common data type is:", result_dtype)
