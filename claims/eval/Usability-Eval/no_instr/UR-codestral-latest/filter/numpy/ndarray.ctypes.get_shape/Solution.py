import numpy as np
import ctypes

def ctypes_array(shape):
    # Determine the base type based on the platform
    if np.dtype('p').itemsize == 4:
        base_type = ctypes.c_int
    elif np.dtype('p').itemsize == 8:
        base_type = ctypes.c_longlong

    # Create the ctypes array
    ctypes_array = (base_type * len(shape))(*shape)

    return ctypes_array

# Example usage
numpy_array = np.random.rand(2, 3, 4)
ctypes_shape = ctypes_array(numpy_array.shape)
