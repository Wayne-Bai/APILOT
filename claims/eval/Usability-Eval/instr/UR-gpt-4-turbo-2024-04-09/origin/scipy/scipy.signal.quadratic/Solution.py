import numpy as np
from scipy.interpolate import BSpline

# Define knots and coefficients for a quadratic B-spline
knots = np.array([0, 1, 2, 3, 4, 5])
coefficients = np.array([1, 2, 3, 4, 5, 6])
degree = 2  # Quadratic

# Create the B-spline object
b_spline = BSpline(knots, coefficients, degree)

# Evaluate the B-spline at some points
x = np.linspace(1, 4, num=100)
y = b_spline(x)

# Print some results
for xi, yi in zip(x, y):
    print(f"B-spline({xi:.2f}) = {yi:.2f}")
