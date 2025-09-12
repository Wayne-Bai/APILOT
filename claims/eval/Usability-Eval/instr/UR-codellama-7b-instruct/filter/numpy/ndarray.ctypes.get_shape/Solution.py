import numpy as np

def get_shape(dtype='p', ndim=None):
    if dtype == 'p':
        base_type = np.ctypeslib.c_intp
    else:
        raise ValueError("Invalid dtype provided")
    return np.ctypeslib.ndpointer(dtype=base_type, shape=ndim)