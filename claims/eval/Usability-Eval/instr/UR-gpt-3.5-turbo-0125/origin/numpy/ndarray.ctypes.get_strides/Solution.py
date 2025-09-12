
import ctypes

class MyArray:
    def __init__(self, shape):
        self.shape = shape
        self.ndim = len(shape)
        self.strides = (ctypes.c_intp * self.ndim)(*shape)

# Example usage
arr = MyArray((3, 4, 5))
print(list(arr.strides))
