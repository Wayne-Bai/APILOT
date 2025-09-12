
import numpy as np
from scipy.interpolate import make_interp_spline

def bspline(x, y, n):
    """
    Generates a B-spline basis function of order n.
    
    Parameters:
        x (array-like): An array of x-coordinates.
        y (array-like): An array of corresponding y-coordinates.
        n (int): The order of the B-spline basis function.
        
    Returns:
        A tuple containing the B-spline basis functions for each point in x and y.
    """
    
    # Generate the knot vector
    t = np.linspace(0, 1, len(x)+n)
    
    # Compute the B-spline coefficients
    coeffs = make_interp_spline(x, y, t, n)
    
    # Evaluate the B-spline at each point in x and y
    xs = np.linspace(0, 1, len(x))
    ys = np.zeros((len(y), len(xs)))
    for i in range(len(y)):
        for j in range(len(xs)):
            ys[i,j] = coeffs[i](xs[j])
    
    return xs, ys
