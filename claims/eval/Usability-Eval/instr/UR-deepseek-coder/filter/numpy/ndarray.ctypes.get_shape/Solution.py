import numpy as np
import ctypes

def create_ctypes_array_from_shape(shape):
    # Determine the appropriate C-integer type for the platform
    if np.dtype('p').itemsize == np.dtype('int').itemsize:
        c_intp = ctypes.c_int
    elif np.dtype('p').itemsize == np.dtype('long').itemsize:
        c_intp = ctypes.c_long
    elif np.dtype('p').itemsize == np.dtype('longlong').itemsize:
        c_intp = ctypes.c_longlong
    else:
        raise ValueError("Unsupported pointer size")

    # Create a ctypes array of the appropriate type and length
    c_array = (c_intp * len(shape))(*shape)
    return c_array

# Example usage
shape = (3, 4, 5)
ctypes_array = create_ctypes_array_from_shape(shape)
print(ctypes_array)
