import numpy as np
import ctypes

def get_strides_ctypes_array(array):
    if not isinstance(array, np.ndarray):
        raise TypeError("The input must be a numpy ndarray.")

    # Get the array strides which provide the bytes to jump to move to the next element
    strides = array.strides
    
    # Determine the type of c_intp based on the platform
    c_intp_type = ctypes.c_long if np.dtype('intp').itemsize == ctypes.sizeof(ctypes.c_long) else ctypes.c_int

    # Create a ctypes array of the strides with c_intp as base type
    c_strides_array = (c_intp_type * array.ndim)(*strides)
    
    return c_strides_array

# Example usage
arr = np.array([[1, 2, 3], [4, 5, 6]])
strides_ctypes_array = get_strides_ctypes_array(arr)

print(strides_ctypes_array[:])  # Prints the strides as a list for readability
