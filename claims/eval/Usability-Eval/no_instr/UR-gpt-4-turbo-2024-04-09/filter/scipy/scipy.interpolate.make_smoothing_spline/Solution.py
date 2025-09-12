import numpy as np
from scipy.interpolate import CubicSpline

def smoothing_cubic_spline(x, y, lam=None):
    if lam is not None:
        # User provided a specific lambda for smoothing
        cs = CubicSpline(x, y, bc_type='natural', smooth=lam)
    else:
        # Use the default smoothing factor (GCV automatically used)
        cs = CubicSpline(x, y, bc_type='natural')
    
    return cs

# Example usage:
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 2.2, 2.8, 3.5, 5])
spline = smoothing_cubic_spline(x, y)

# Display the coefficients of the spline
print("Coefficients of cubic spline:", spline.c)
