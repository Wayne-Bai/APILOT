
import numpy as np

def get_ctypes_array(self):
    # Create a ctypes array of length self.ndim
    arr = (ctypes.c_int * self.ndim)()
    for i in range(self.ndim):
        arr[i] = ctypes.c_int(self.shape[i])
    return arr
