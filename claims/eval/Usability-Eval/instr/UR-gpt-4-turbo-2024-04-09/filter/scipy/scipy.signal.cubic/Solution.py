import numpy as np
from scipy.interpolate import BSpline

# Define knots, coefficients, and the degree of the spline
knots = np.array([0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4])
coefficients = np.array([0, 1, 0, -1, 0])  # example coefficients
k = 3  # Cubic spline

# Create a cubic B-spline object
cubic_spline = BSpline(knots, coefficients, k)

# Evaluate the spline at specific points
x = np.linspace(0, 4, 100)
y = cubic_spline(x)

# The x and y arrays now contain the x coordinates and corresponding spline values
print(y)
