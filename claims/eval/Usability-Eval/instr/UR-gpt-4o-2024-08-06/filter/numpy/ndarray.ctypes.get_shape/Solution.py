import numpy as np
import ctypes

# Create a numpy array as an example
array = np.array([[1, 2, 3], [4, 5, 6]])

# Get the number of dimensions of the array
ndim = array.ndim

# Determine the appropriate C integer type for the platform
c_intp = np.ctypeslib.ctypes.c_int if np.dtype('p').itemsize == ctypes.sizeof(ctypes.c_int) else (
    np.ctypeslib.ctypes.c_long if np.dtype('p').itemsize == ctypes.sizeof(ctypes.c_long) else ctypes.c_longlong
)

# Create a ctypes array of shape with the determined base type
shape_ctypes_array = (c_intp * ndim)(*array.shape)

# Output the ctypes array
print(shape_ctypes_array)
