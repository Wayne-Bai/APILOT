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
    array-like: The values of the B-spline basis functions at the points x.
    """
    # Ensure the knots are sorted
    knots = np.sort(knots)
    
    # Create the B-spline basis functions
    basis_functions = []
    for i in range(len(knots) - degree - 1):
        coeffs = np.zeros(len(knots) - degree - 1)
        coeffs[i] = 1.0
        bspline = BSpline(knots, coeffs, degree)
        basis_functions.append(bspline(x))
    
    return np.array(basis_functions)

# Example usage:
x = np.linspace(0, 1, 100)
knots = np.array([0, 0, 0, 0.5, 1, 1, 1])
degree = 2
basis = bspline_basis(x, knots, degree)

print(basis)
