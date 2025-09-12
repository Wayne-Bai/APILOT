import numpy as np
from scipy.integrate import simps

def integrate_with_simpsons_rule(y, x=None):
    if x is None:
        dx = 1  # default spacing
        x = np.arange(len(y)) * dx
    return simps(y, x)
