import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define a set of knots
knots = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# Define coefficients for the B-spline basis functions
coefficients = np.array([0, 0, 1, 2, 1, 0, 0])

# The degree of the B-spline
degree = 3

# Create a B-spline representation
spline = BSpline(knots, coefficients, degree)

# Create a range of x values for which to evaluate the B-spline
x_values = np.linspace(knots[degree], knots[-degree-1], 100)

# Evaluate the B-spline at each x value
y_values = spline(x_values)

# Plot the B-spline
plt.plot(x_values, y_values, label='Cubic B-spline')
plt.title('Cubic B-spline Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
