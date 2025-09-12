
import ctypes as ct
import numpy as np

# Define a function to create a ctypes array for the shape
def create_shape_array(ndim):
    # Get the basetype corresponding to dtype('p') on this platform
    intp = np.dtype('p').basetype

    # Create an empty ctypes array with the correct size and basetype
    return (ct.c_intp * ndim)(*[intp() for _ in range(ndim)])

# Define a function to create a ctypes array for the strides
def create_stride_array(shape, itemsize):
    # Get the basetype corresponding to dtype('p') on this platform
    intp = np.dtype('p').basetype

    # Create an empty ctypes array with the correct size and basetype
    return (ct.c_intp * len(shape))(*[intp() for _ in range(len(shape))])

# Define a function to create a ctypes array for the data pointer
def create_dataptr_array():
    # Get the basetype corresponding to dtype('p') on this platform
    intp = np.dtype('p').basetype

    # Create an empty ctypes array with the correct size and basetype
    return (ct.c_intp * 1)()

# Define a function to create a ctypes array for the suboffsets
def create_suboffsets_array(ndim):
    # Get the basetype corresponding to dtype('p') on this platform
    intp = np.dtype('p').basetype

    # Create an empty ctypes array with the correct size and basetype
    return (ct.c_intp * ndim)(*[intp() for _ in range(ndim)])
