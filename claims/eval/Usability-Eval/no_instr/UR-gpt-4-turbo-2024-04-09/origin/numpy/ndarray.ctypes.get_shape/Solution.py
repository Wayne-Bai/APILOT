import numpy as np
import ctypes

# Get the appropriate ctypes integer type for the platform addressing
if np.dtype('p').kind == 'i':
    if np.dtype('p').itemsize == 4:
        c_intp = ctypes.c_int
    elif np.dtype('p').itemsize == 8:
        c_intp = ctypes.c_longlong
else:
    # commonly on many platforms np.dtype('p') is equivalent to np.intp, and fits ctypes.c_long
    c_intp = ctypes.c_long

# Example: Let's assume we have an ndim and a shape
ndim = 3
array_shape = (10, 20, 30)  

# Create ctypes array of type c_intp with length ndim and initialize with array_shape
shape_ctypes = (c_intp * ndim)(*array_shape)

print("Shape as ctypes array:", list(shape_ctypes))
