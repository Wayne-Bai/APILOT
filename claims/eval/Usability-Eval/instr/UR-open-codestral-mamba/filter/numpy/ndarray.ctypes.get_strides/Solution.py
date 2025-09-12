import numpy as np

class MyClass:
    def __init__(self, ndim, shape):
        self.ndim = ndim
        self.shape = shape
        self.strides = np.ctypeslib._nd_pointer(np.intp, (self.ndim,), {'shape': self.shape})()

# Example usage
my_obj = MyClass(2, (3, 4))
print(my_obj.strides)
