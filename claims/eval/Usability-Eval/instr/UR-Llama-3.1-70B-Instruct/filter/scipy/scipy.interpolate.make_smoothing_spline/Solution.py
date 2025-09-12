import numpy as np
from scipy.interpolate import UnivariateSpline

def compute_cubic_spline(x, y, lam=None):
    """
    Compute the coefficients of smoothing cubic spline function.

    Parameters:
    x (array_like):Input data points.
    y (array_like):Input data values.
    lam (float, optional): Control the tradeoff between smoothness and proximity to data. 
                           If None, use the GCV criteria to find it. Default is None.

    Returns:
    tck (tuple): A tuple (t, c, k) containing the coefficients of the smoothing cubic spline.
    """

    # Create a UnivariateSpline object with the input data
    spline = UnivariateSpline(x, y, s=lam)

    # Get the coefficients of the cubic spline
    tck = spline._eval_args

    return tck

# Example usage:
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) / 10  # Add some noise to the data

# Compute the coefficients of the smoothing cubic spline with a specified lambda
tck = compute_cubic_spline(x, y, lam=0.01)

# Compute the coefficients of the smoothing cubic spline using the GCV criteria
tck_gcv = compute_cubic_spline(x, y)
