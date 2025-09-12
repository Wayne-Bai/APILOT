import numpy as np
from scipy.special import eval_legendre

def quadratic_b_spline(x):
    """
    This function calculates the quadratic B-spline for a given input x.

    Parameters:
    x (array-like): The input values for which the B-spline is calculated.

    Returns:
    array-like: The calculated B-spline values.
    """
    # Calculate the B-spline coefficients
    b_coeffs = np.array([1/6, 2/3, 1/6])

    # Calculate the B-spline values using the coefficients and the input x
    b_spline_values = np.sum(b_coeffs * eval_legendre(x))

    return b_spline_values
