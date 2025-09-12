import numpy as np
from ctypes import c_intptr

class MyArray:
    def __init__(self, array):
        self.array = array
        self.shape = array.shape
        self.ndim = array.ndim
        self.strides = array.strides

    @property
    def ctypes_strides(self):
        max_size = np.iinfo(np.int64).max
        # Create a ctypes array with the appropriate number of elements and type.
        strides_array = np.ctypeslib.c_apr(self.ndim, c_intptr, self.strides)
        # Replace np.ctypeslib.c_apr if its use is deprecated.
        strides_array[:] = strides_array.as_ptr()

        return strides_array

# Example usage
arr = np.array([[1, 2], [3, 4]], dtype=np.int64)
my_array = MyArray(arr)
strides = my_array.ctypes_strides
print(strides)
