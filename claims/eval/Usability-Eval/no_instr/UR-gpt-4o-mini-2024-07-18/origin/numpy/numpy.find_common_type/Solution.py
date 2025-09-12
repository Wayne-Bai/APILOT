import numpy as np

def common_type(arrays):
    # Determine the common data type by using NumPy's broadcasting rules
    return np.find_common_type([arr.dtype for arr in arrays], [])

# Example usage
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
array3 = np.array(['a', 'b', 'c'], dtype=np.str_)

common_dtype = common_type([array1, array2, array3])
print("Common data type:", common_dtype)
