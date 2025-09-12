import numpy as np

class MyArray:
    def __init__(self, shape, dtype):
        self.shape = shape
        self.dtype = dtype
        self.ndim = len(shape)
        self.ctypes_strides = np.dtype(dtype).itemsize * np.c_intp * self.ndim
