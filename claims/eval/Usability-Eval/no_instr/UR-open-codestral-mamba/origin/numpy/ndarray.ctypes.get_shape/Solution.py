import numpy as np
from ctypes import c_intp

class MyArray:
    def __init__(self, shape):
        self.shape = shape
        self.ndim = len(shape)

# Create a MyArray object
my_array = MyArray((3, 4, 5))

# Create a ctypes array
ctypes_array = (c_intp * my_array.ndim)(*my_array.shape)

print(ctypes_array)
