import numpy as np
from scipy.integrate import simps

def integrate_y(y, x=None, dx=None):
    if x is None:
        if dx is None:
            raise ValueError("Either x or dx must be provided.")
        x = np.arange(len(y)) * dx
    else:
        if dx is not None:
            raise ValueError("Either x or dx must be provided, not both.")
    return simps(y, x)
