import numpy as np
from scipy.interpolate import CubicSpline

# Assuming x and y are your data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# If lam is None, use GCV criteria to find it
if lam is None:
    cs = CubicSpline(x, y, bc_type='natural', extrapolate=None)
    lam = cs.get_residual()

# Compute the smoothing cubic spline function with lam
cs = CubicSpline(x, y, bc_type='natural', extrapolate=None, k=3, lam=lam)

# Now you can use cs to compute the spline function
x_new = np.linspace(1, 5, 100)
y_new = cs(x_new)
