import numpy as np
from scipy.interpolate import BSpline

def bspline_basis(x, knots, degree):
    """
    Compute the B-spline basis function of a given degree.

    Parameters:
    x (array-like): The points at which to evaluate the basis functions.
    knots (array-like): The knot vector.
    degree (int): The degree of the B-spline.

    Returns:
    array: The values of the B-spline basis functions at the points x.
    """
    # Ensure the knots are in the correct format
    knots = np.asarray(knots)
    # Create the B-spline basis function
    bspline = BSpline(knots, np.ones_like(knots), degree)
    # Evaluate the basis function at the points x
    return bspline(x)

# Example usage:
x = np.linspace(0, 1, 100)
knots = [0, 0, 0, 0.5, 1, 1, 1]
degree = 2
basis_values = bspline_basis(x, knots, degree)
print(basis_values)
