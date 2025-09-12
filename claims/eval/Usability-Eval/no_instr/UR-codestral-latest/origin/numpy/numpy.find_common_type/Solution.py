import numpy as np

# Let's assume we have the following numpy arrays
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)

# To find the common type that would accommodate both arrays
common_type = np.result_type(array1.dtype, array2.dtype)

print(f'The common type is: {common_type}')
