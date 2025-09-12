
import numpy as np

# Define a function to get the strides information
def get_strides(arr):
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array")

    strides_info = arr.strides
    ctypes_array = (arr.__array_interface__['data'][0] + np.arange(arr.ndim) * strides_info[0]).astype(np.intp)

    return ctypes_array

# Test the function
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
strides_array = get_strides(arr)
print(strides_array)
