import numpy as np

def generate_strides_info(self):
    return np.ctypeslib.ndpointer(dtype=self.dtype, ndim=self.ndim, flags='C_CONTIGUOUS')
