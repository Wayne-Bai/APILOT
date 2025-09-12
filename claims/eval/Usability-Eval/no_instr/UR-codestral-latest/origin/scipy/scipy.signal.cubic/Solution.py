from scipy import interpolate
import numpy as np

# Define the control points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 0, 1, 3, 2])

# Define the knots
t = np.array([0, 0, 0, 1, 2, 3, 4, 5, 5, 5])

# Create the cubic B-spline
spline = interpolate.BSpline(t, y, k=3)

# Generate x-coordinates for the smooth curve
x_new = np.linspace(0, 5, 100)

# Evaluate the B-spline at the new x-coordinates
y_new = spline(x_new)
