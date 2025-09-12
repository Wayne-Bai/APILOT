import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

# Define the knots, coefficients and degree for a cubic B-spline
knots = [0, 1, 2, 3, 4, 5]  # Example knots
coefficients = [1, 0, 0, 1]  # Example coefficients for the spline
degree = 3  # Cubic B-spline

# Create the B-spline representation
cubic_bspline = BSpline(knots, coefficients, degree)

# Evaluate the B-spline at specific points
x_values = np.linspace(0, 5, 100)  # Evaluate points
y_values = cubic_bspline(x_values)

# For visualization purposes (if needed)
import matplotlib.pyplot as plt

plt.plot(x_values, y_values, label='Cubic B-Spline')
plt.title('Cubic B-Spline Illustration')
plt.xlabel('x')
plt.ylabel('B-Spline Value')
plt.legend()
plt.grid()
plt.show()
