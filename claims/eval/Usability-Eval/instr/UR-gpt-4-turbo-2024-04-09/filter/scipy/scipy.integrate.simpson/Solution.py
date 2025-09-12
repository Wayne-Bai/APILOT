import numpy as np
from scipy.integrate import simps

def integrate_using_simps(y, x=None, dx=1.0):
    """Integrate y(x) using the composite Simpson's rule.
    
    Args:
    y : array_like
        Array of sample y values.
    x : array_like, optional
        Array of x positions corresponding to y values. If none, uniform spacing of dx is assumed.
    dx : float, optional
        Spacing of the samples. This argument is only used if x is None.
    
    Returns:
    float
        Approximate integral of y(x).
    """
    if x is None:
        result = simps(y, dx=dx)
    else:
        result = simps(y, x)
    return result
