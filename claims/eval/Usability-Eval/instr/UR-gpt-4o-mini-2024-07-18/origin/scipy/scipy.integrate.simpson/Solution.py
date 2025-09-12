import numpy as np
from scipy.integrate import simps

def integrate_y(x, y, dx=None):
    if x is None:
        # If x is not provided, generate x based on the length of y and spacing dx
        x = np.arange(len(y)) * dx if dx is not None else np.arange(len(y))
    
    # Use composite Simpson's rule to integrate y
    result = simps(y, x)
    return result
