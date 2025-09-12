import numpy as np
from scipy.interpolate import BSpline

# Assuming x is your data
x = np.array([1, 2, 3, 4, 5])

# Create a cubic B-spline
bspline = BSpline(x, 3)

# Evaluate the B-spline at new points
new_points = np.linspace(1, 5, 100)
y = bspline(new_points)
