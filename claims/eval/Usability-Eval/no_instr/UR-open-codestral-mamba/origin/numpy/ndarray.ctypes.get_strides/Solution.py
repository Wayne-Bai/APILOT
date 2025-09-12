import numpy as np
from ctypes import c_intp, py_object

# assuming that 'self' is an instance of a numpy array
class MyArray:
    def __init__(self, myarray):
        self.myarray = myarray
        self.ndim = myarray.ndim
        self.shape = myarray.shape

    def c_intp_ndim(self):
        return (c_intp * self.ndim)(*self.shape)

    def strides_information(self):
        return self.myarray.strides
