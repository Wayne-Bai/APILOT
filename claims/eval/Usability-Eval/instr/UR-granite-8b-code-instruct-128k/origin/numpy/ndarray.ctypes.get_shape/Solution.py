import numpy as np

def generate_ctypes_array(self):
    return np.ctypeslib.as_ctypes(self.shape)
