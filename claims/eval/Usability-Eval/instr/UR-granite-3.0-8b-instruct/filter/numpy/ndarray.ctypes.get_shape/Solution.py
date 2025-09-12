import numpy as np

class MyClass:
    def __init__(self, shape):
        self.shape = shape
        self.ndim = len(shape)
        self.dtype = np.dtype('p')  # This will give the C-integer corresponding to dtype('p') on this platform
        self.c_intp_shape = np.ctypeslib.as_ctypes(np.array(self.shape, dtype=self.dtype))
