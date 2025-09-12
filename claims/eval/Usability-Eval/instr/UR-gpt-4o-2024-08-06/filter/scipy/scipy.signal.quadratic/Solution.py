import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define knot vector and coefficients for quadratic B-spline
knots = np.array([0, 1, 2, 3, 4, 5, 6])  # Must be non-decreasing
coefficients = np.array([0, 1, 2, 1, 0])  # Example coefficients
degree = 2  # Quadratic B-spline

# Create the B-spline object
b_spline = BSpline(knots, coefficients, degree)

# Points to evaluate the B-spline
x_values = np.linspace(0, 6, 100)

# Evaluate the B-spline
y_values = b_spline(x_values)

# Plot the B-spline
plt.plot(x_values, y_values, label="Quadratic B-spline")
plt.title("Quadratic B-spline Curve")
plt.xlabel("x")
plt.ylabel("B-spline value")
plt.grid()
plt.legend()
plt.show()
