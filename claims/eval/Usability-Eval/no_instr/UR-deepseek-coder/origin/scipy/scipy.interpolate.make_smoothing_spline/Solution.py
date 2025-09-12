import numpy as np
from scipy.interpolate import UnivariateSpline

def compute_smoothing_spline(x, y, lam=None):
    """
    Compute the coefficients of a smoothing cubic spline function.

    Parameters:
    x (array-like): Input data points.
    y (array-like): Corresponding values.
    lam (float, optional): Smoothing parameter. If None, GCV is used to find it.

    Returns:
    UnivariateSpline: A smoothing spline fitted to the data.
    """
    if lam is None:
        # Use GCV to find the optimal lambda
        def gcv(l):
            spl = UnivariateSpline(x, y, s=l)
            y_fit = spl(x)
            mse = np.mean((y - y_fit) ** 2)
            trace_S = np.sum(spl.get_coeffs() != 0)
            return mse / (1 - (trace_S / len(x))) ** 2

        # Grid search for lambda
        lam_values = np.logspace(-3, 3, 7)
        gcv_values = [gcv(l) for l in lam_values]
        lam = lam_values[np.argmin(gcv_values)]

    # Fit the smoothing spline with the chosen lambda
    spl = UnivariateSpline(x, y, s=lam)
    return spl

# Example usage:
# x = np.linspace(0, 10, 100)
# y = np.sin(x) + np.random.normal(0, 0.1, 100)
# spline = compute_smoothing_spline(x, y)
# y_fit = spline(x)
