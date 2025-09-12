import numpy as np
from scipy import interpolate

def B_spline_basis(n, knots, x):
    """
    Compute the B-spline basis function of order n.

    Parameters:
    n (int): The order of the basis function.
    knots (list or np.ndarray): The knots of the basis function. The knots are supposed to be sorted (in ascending or descending order)
    x (float or list or np.ndarray): The input values for which to compute the B-spline basis function.

    Returns:
    numpy.ndarray: The B-spline basis function of order n evaluated at x.
    """
    if isinstance(x, (list, np.ndarray)):
        basis = np.empty((len(x), len(knots)-n-1))
        for i, xi in enumerate(x):
            basis[i] = interpolate.BSpline.basis_element(knots)(xi)
    else:
        basis = interpolate.BSpline.basis_element(knots)(x)
    return basis

