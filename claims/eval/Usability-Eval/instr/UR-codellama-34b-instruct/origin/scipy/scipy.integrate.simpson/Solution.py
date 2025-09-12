import numpy as np
from scipy.integrate import simps

def integrate_simpsons_rule(y, x=None, dx=None):
    """
    Integrates y(x) using samples along the given axis and the composite Simpson's rule.
    If x is None, spacing of dx is assumed.
    
    Args:
        y (numpy array): Function values at each point in the interval.
        x (numpy array or float): Coordinates of points to be used for integration.
                                Default is None.
        dx (float): Spacing between points if x is not given. Default is None.
    
    Returns:
        I (float): Integral of y(x) using the composite Simpson's rule.
    """
    # If no coordinates are given, assume equal spacing between points
    if x is None and dx is not None:
        x = np.arange(0, len(y), dx)
    
    # Initialize the sum for the integral
    I = 0
    
    # Loop over each interval and add contributions to the sum
    for i in range(len(x)-1):
        I += (simps(y[i], x[i]) + simps(y[i+1], x[i+1])) * dx[i] / 2
    
    # Return the final integral value
    return I
