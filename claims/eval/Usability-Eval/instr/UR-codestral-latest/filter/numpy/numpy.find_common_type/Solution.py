import numpy as np

# These are your example arrays
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([4, 5, 6], dtype=np.float64)

# Determine the common type
common_type = np.find_common_type([array1.dtype, array2.dtype], [])

print('The common type is:', common_type)
