import numpy as np
from scipy.interpolate import interp1d

# Define the knots
knots = np.array([0, 0, 0, 1, 2, 3, 3, 3])

# Define the control points
ctrl_points = np.array([[0, 0], [1, 2], [2, 1], [3, 0]])

# Create the cubic B-spline
bspline = interp1d(knots, ctrl_points, kind='cubic', axis=0)

# Evaluate the B-spline at x = 1.5
x = 1.5
y = bspline(x)

print(f'The value of the cubic B-spline at x = {x} is {y}')
