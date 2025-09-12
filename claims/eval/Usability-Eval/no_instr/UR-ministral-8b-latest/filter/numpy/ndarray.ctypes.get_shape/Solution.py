import numpy as np
import ctypes

# Function to determine the ctypes integer type that corresponds to numpy.DataType.DTYPE['p']
def get_ctypes_int_type():
    if np.dtype('64').itemsize == 8:
        return ctypes.c_long
    elif np.dtype('4').itemsize == 4:
        return ctypes.c_int
    else:
        return ctypes.c_longlong

# Calculate the shape and convert it to appropriate ctypes array
class ArrayShapeCTypes:
    def __init__(self, ndim):
        self.ndim = ndim
        self.shape = ctypes.c_intp * self.ndim

    def get_shape(self):
        primitive_ctypes_int_type = get_ctypes_int_type()
        shape_array = np.array(list(range(self.ndim))).astype(primitive_ctypes_int_type)
        return shape_array

# Usage example
ndim = 3
array_shape = ArrayShapeCTypes(ndim).get_shape()
print(array_shape)
