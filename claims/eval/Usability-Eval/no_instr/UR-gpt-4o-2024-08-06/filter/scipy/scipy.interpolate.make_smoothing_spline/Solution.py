from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.linspace(0, 10, 10)
y = np.sin(x)

def smoothing_cubic_spline(x, y, lam=None):
    """
    Compute the coefficients of the smoothing cubic spline.
    
    Parameters:
    x (array-like): Independent variable data points.
    y (array-like): Dependent variable data points.
    lam (float or None): Smoothing factor. If None, use GCV to estimate the smoothing parameter.
    
    Returns:
    spline : UnivariateSpline object
    """
    if lam is None:
        # Use UnivariateSpline with default smoothness (GCV criteria)
        spline = UnivariateSpline(x, y, s=None)
    else:
        # Use specified smoothing factor lambda
        spline = UnivariateSpline(x, y, s=lam)
    return spline

# Compute the spline
spline = smoothing_cubic_spline(x, y)

# Example usage of the spline
x_fine = np.linspace(0, 10, 100)
y_spline = spline(x_fine)

# Plot the results
plt.scatter(x, y, label='Data Points')
plt.plot(x_fine, y_spline, label='Smoothing Cubic Spline', color='red')
plt.legend()
plt.show()
