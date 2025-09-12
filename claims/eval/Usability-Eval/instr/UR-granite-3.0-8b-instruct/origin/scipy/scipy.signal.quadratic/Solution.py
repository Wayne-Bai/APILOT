import numpy as np
from scipy.interpolate import BSpline

# Define the knots for the quadratic B-spline
knots = np.array([0, 0, 0, 1, 2, 3, 3, 3])

# Define the coefficients for the quadratic B-spline
coefficients = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Create the quadratic B-spline
bspline = BSpline(knots, coefficients, deg=2)

# Evaluate the quadratic B-spline at x = 1.5
x = 1.5
y = bspline(x)

print(f"The value of the quadratic B-spline at x = {x} is {y}")
