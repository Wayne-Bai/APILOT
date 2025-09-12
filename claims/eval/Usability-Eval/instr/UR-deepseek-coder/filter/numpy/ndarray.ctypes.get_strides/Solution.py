import numpy as np
import ctypes

class ArrayStrides:
    def __init__(self, array):
        self.array = array
        self.ndim = array.ndim
        self.shape = array.shape
        self.strides = array.strides

    def get_strides_ctypes_array(self):
        # Create a ctypes array of length self.ndim with the same basetype as the shape attribute
        c_intp = ctypes.c_ssize_t * self.ndim
        strides_array = c_intp(*self.strides)
        return strides_array

# Example usage
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
array_strides = ArrayStrides(arr)
strides_ctypes_array = array_strides.get_strides_ctypes_array()
print(strides_ctypes_array)
