import numpy as np

def determine_common_type(*arrays):
    common_dtype = np.find_common_type([arr.dtype for arr in arrays], [])
    return common_dtype

# Example usage:
arr1 = np.array([1, 2, 3], dtype=np.int32)
arr2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
arr3 = np.array(['a', 'b', 'c'], dtype='<U1')

common_type = determine_common_type(arr1, arr2, arr3)
print(common_type)
