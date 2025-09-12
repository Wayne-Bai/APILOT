import numpy as np
import ctypes

class StrideArray:
    def __init__(self, array):
        self.array = array
        self.ndim = array.ndim
        self.strides = self.array.strides

    def get_strides_ctypes(self):
        # Create a ctypes array with the same basetype as the shape attribute
        strides_ctypes = (ctypes.c_intp * self.ndim)(*self.strides)
        return strides_ctypes

# Example usage
array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
stride_array = StrideArray(array)
ctypes_strides = stride_array.get_strides_ctypes()
print(ctypes_strides)
