import numpy as np
from scipy.interpolate import make_interp_spline

# Define the x and y values for the spline
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Create a quadratic B-spline object
spline = make_interp_spline(x, y, k=2)

# Evaluate the spline at some points
points = np.linspace(0, 4, 10)
values = spline(points)
