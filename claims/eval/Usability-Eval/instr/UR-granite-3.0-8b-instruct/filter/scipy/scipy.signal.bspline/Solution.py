import numpy as np
from scipy.interpolate import BSpline

def bspline_basis_function(x, n, knots):
    """
    Calculate the B-spline basis function of order n.

    Parameters:
    x (float): The point at which to evaluate the basis function.
    n (int): The order of the B-spline.
    knots (numpy array): The knots for the B-spline.

    Returns:
    float: The value of the B-spline basis function at x.
    """
    # Create a B-spline object with the given order and knots
    bspline = BSpline(knots, np.linspace(0, 1, len(knots)), n - 1)

    # Evaluate the B-spline at x
    return bspline(x)
