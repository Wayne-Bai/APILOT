
import numpy as np

def get_strides(arr):
    # Get the shape of the array
    shape = arr.shape
    # Get the strides information from the underlying array
    strides = arr.strides
    # Create a ctypes array of length self.ndim where the basetype is the same as for the shape attribute
    strides_ctypes = (c_intp * self.ndim)()
    # Fill in the values from the strides information
    for i in range(self.ndim):
        strides_ctypes[i] = strides[i]
    return strides_ctypes
