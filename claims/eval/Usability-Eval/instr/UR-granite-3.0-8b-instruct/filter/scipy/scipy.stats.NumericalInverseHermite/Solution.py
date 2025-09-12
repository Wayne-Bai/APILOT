import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.special import erf

def inv_hermite_spline_cdf(cdf, order=3):
    """
    Approximates the inverse of a continuous statistical distribution's CDF with a Hermite spline.

    Parameters:
    cdf (callable): The CDF of the distribution.
    order (int, optional): The order of the Hermite spline. Default is 3.

    Returns:
    callable: The inverse of the CDF.
    """
    # Generate the Hermite spline coefficients
    t = np.linspace(0, 1, 1000)
    y = cdf(t)
    dy = np.gradient(y, t)
    d2y = np.gradient(dy, t)
    coeffs = np.polyfit(t, y, order)

    # Construct the Hermite spline
    hermite_spline = InterpolatedUnivariateSpline(t, y, k=order, ext=0)

    # Define the inverse CDF
    inv_cdf = lambda u: hermite_spline(erf(u)**2)

    return inv_cdf
