import numpy as np
from scipy import integrate

def integrator(y, x=None, dx=1.0):
    if x is None:
        return integrate.simps(y, dx=dx)
    else:
        return integrate.simps(y, x)
