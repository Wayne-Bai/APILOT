import numpy as np

class MyArray:
    def __init__(self, shape, strides):
        self.shape = shape
        self.strides = strides

    def get_strides(self):
        return tuple(c_intp * self.ndim for c_intp in self.strides)

# Example usage:
shape = (3, 4)
strides = (12, 3)
my_array = MyArray(shape, strides)
print(my_array.get_strides())
