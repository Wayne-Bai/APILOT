
import numpy as np

def get_strides(self):
    return np.ctypeslib.as_ctypes(self.strides)
