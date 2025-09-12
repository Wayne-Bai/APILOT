import numpy as np

class MyArray:
    def __init__(self, shape):
        self.shape = shape
        self.ndim = len(shape)
        self.strides = np.ctypeslib.as_ctypes(np.array(shape))

my_array = MyArray((3, 4, 5))
print(my_array.strides)
