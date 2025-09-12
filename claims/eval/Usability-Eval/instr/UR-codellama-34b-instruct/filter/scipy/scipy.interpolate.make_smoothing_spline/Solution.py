import numpy as np
from scipy.interpolate import CubicSpline

# Generate some random data for demonstration purposes
n = 10
x = np.linspace(0, 1, n)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.normal(size=n)

# Define the smoothing parameter lam (if not provided, use GCV criteria to find it)
lam = None if None else 1e-3

# Compute the coefficients of the cubic spline function using scipy
cs = CubicSpline(x, y, lam=lam)

# Evaluate the smoothed curve at new points
new_x = np.linspace(0, 1, 100)
new_y = cs(new_x)
