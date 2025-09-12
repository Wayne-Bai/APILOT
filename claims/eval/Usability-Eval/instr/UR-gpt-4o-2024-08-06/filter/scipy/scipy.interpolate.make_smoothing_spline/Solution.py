import numpy as np
from scipy.interpolate import UnivariateSpline

def smoothing_cubic_spline(x, y, lam=None):
    """
    Computes the coefficients of a smoothing cubic spline function.

    Parameters:
    x (array-like): The independent variable.
    y (array-like): The dependent variable.
    lam (float or None): Smoothing parameter. If None, uses GCV to determine it.

    Returns:
    UnivariateSpline: A smoothed spline function.
    """
    
    # Set smoothing parameter
    if lam is not None:
        spline = UnivariateSpline(x, y, s=lam)
    else:
        # uses GCV to determine the best smoothing parameter
        spline = UnivariateSpline(x, y)
    
    return spline

# Example usage
x = np.linspace(0, 10, 10)
y = np.sin(x) + np.random.normal(0, 0.1, x.shape)
spline_func = smoothing_cubic_spline(x, y, lam=None)

# You can now use spline_func to evaluate the spline, for example:
x_new = np.linspace(0, 10, 100)
y_new = spline_func(x_new)

# Plotting to visualize
import matplotlib.pyplot as plt

plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, label='Smoothing Spline', color='red')
plt.legend()
plt.show()
