
import numpy as np

def cumprod(a, axis=None):
    if axis is None:
        return np.cumprod(a.ravel())
    else:
        return np.apply_along_axis(np.cumprod, axis, a)
