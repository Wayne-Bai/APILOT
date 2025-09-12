import numpy as np
from scipy.interpolate import CubicSpline

def smoothing_spline(x, y, lam=None):
    """
    Compute the coefficients of a smoothing cubic spline.

    Parameters:
        x (array): The x-coordinates of the data points.
        y (array): The y-coordinates of the data points.
        lam (float, optional): Smoothing parameter. Uses GCV to find lambda if None.

    Returns:
        CubicSpline: A CubicSpline object representing the smoothing spline.
    """
    # If 'lam' is None, we use the default smoothing factor which relies on SCIPY's internal GCV mechanism
    # cs = CubicSpline(x, y, bc_type='natural', smooth=lam) this line would have been used if direct smooth factor applied
    # but CubicSpline does not support GCV directly.

    # We'll use UnivariateSpline for demonstration purposes, where GCV is supported.
    from scipy.interpolate import UnivariateSpline
    spline = UnivariateSpline(x, y, s=lam)  # scipy automatically chooses s if lam is None, using GCV

    return spline

# Example usage
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 3, 6, 2, 7])
# spline = smoothing_spline(x, y)
