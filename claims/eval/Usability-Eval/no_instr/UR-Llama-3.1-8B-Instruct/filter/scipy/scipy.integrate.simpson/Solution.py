import numpy as np
from scipy.integrate import quad, trapz
from scipy.interpolate import CubicSpline

def composite_simpsons_rule(x, y, dx):
    """
    Integrate y(x) using composite Simpson's rule.

    Parameters:
    x (numpy array): Array of sample points along the axis.
    y (numpy array): Array of function values at sample points.
    dx (float): Spacing of the sample points.

    Returns:
    float: The approximate integral of y(x) from x[0] to x[-1].
    """
    n = len(x)
    a = x[0]
    b = x[-1]
    
    if (n % 2!= 0):
        raise ValueError("The number of points must be even")

    integral = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    integral *= dx / 3

    return integral
