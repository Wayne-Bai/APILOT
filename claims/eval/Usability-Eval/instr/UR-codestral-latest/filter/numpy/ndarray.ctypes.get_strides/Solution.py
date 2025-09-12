import numpy as np
import ctypes

class MyClass:
    def __init__(self, array):
        self.array = array
        self.ndim = array.ndim
        self.strides = array.strides

    def get_strides(self):
        return (ctypes.c_int * self.ndim)(*self.strides)

# Create object and test the function
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
obj = MyClass(arr)
print(obj.get_strides())
