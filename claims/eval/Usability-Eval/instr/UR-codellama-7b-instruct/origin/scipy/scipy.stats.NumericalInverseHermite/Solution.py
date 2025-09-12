
from scipy import interpolate
import numpy as np

def approx_inverse_cdf(cdf, x0, y0):
    """Approximates the inverse of a continuous statistical distribution's CDF with a Hermite spline.

    Args:
        cdf (function): The cumulative distribution function of the statistical distribution.
        x0 (ndarray): The input values for which the CDF is computed.
        y0 (ndarray): The output values corresponding to the CDF evaluated at x0.
        order (int, optional): The order of the Hermite spline approximation. Defaults to 3.

    Returns:
        interpolate.HermiteSpline: A Hermite spline approximation of the inverse of the CDF.
    """
    # Create a list of knots
    x_knots = np.linspace(x0[0], x0[-1], 100)
    y_knots = cdf(x_knots)

    # Create a Hermite spline
    hermite_spline = interpolate.HermiteSpline(x_knots, y_knots, order=3)

    return hermite_spline
