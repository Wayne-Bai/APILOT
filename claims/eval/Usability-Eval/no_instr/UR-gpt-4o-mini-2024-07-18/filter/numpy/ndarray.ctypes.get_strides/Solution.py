import numpy as np
import ctypes

class MyArray:
    def __init__(self, array):
        self.array = np.array(array)
        self.ndim = self.array.ndim
        self.strides = self.array.strides

    def get_ctypes_strides(self):
        # Create a ctypes array of length self.ndim
        strides_ctypes = (ctypes.c_intp * self.ndim)(*self.strides)
        return strides_ctypes

# Example usage
my_array = MyArray([[1, 2, 3], [4, 5, 6]])
ctypes_strides = my_array.get_ctypes_strides()
print(ctypes_strides)
