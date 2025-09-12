
import numpy as np
from scipy.interpolate import make_interp_spline

def quadratic_bspline(x, y):
    """
    Create a quadratic B-spline interpolation function based on the given x and y values.

    Parameters
    ----------
    x : array_like
        The input values to be interpolated.
    y : array_like
        The corresponding output values to be interpolated.

    Returns
    -------
    spline : Callable
        A callable function that takes a single argument and returns the interpolated value.
    """
    # Create the knots for the B-spline interpolation
    knots = np.linspace(x.min(), x.max(), num=len(x) + 2, endpoint=True)

    # Create the B-spline coefficients using natural spline basis
    b_coeffs = make_interp_spline(knots, y, method="natural")[1]

    # Define the quadratic B-spline interpolation function
    def spline(x):
        """Interpolate the data at x"""
        # Find the knot index that contains x
        i = np.searchsorted(knots, x, side="left")

        # Evaluate the B-spline coefficients using the specified method
        y_interp = b_coeffs[i - 1](x) + b_coeffs[i](x) * (x - knots[i - 1]) + b_coeffs[i + 1](x) * (knots[i + 1] - x)

        return y_interp

    return spline
