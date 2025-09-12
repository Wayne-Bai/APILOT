import numpy as np
from scipy.interpolate import BSpline

def b_spline_basis_function(n, k, t):
    """
    Generate a B-spline basis function of order n at k given a knot vector t.

    Parameters:
    n (int): Order of the B-spline.
    k (int): Index of the basis function.
    t (array-like): Knot vector.

    Returns:
    BSpline: The B-spline basis function of order n.
    """
    # Generate the coefficients for the B-spline basis function
    coefficients = np.zeros(len(t) - n)  # Number of coefficients is number of intervals
    coefficients[k] = 1

    # Create the B-spline basis function
    b_spline = BSpline(t, coefficients, n)

    return b_spline

# Example usage
k = 2  # Index of the basis function
n = 3  # Order of the B-spline
t = [0, 0, 0, 1, 2, 3, 3, 3]  # Knot vector

b_spline_function = b_spline_basis_function(n, k, t)
print(b_spline_function)
