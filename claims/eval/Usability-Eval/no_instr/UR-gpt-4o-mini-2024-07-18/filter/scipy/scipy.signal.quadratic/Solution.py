import numpy as np
from scipy.interpolate import BSpline

# Define the knots, coefficients (control points), and degree for the B-spline
knots = np.array([0, 0, 0, 1, 2, 2, 2])  # Knot vector for a quadratic B-spline
coefficients = np.array([1, 2, 3, 4])   # Control points
degree = 2                               # Degree of the B-spline

# Create the B-spline
spline = BSpline(knots, coefficients, degree)

# Define a range of x values for evaluation
x_values = np.linspace(0, 2, 100)

# Evaluate the B-spline at the given x values
y_values = spline(x_values)

# Optionally, you can visualize the B-spline using matplotlib
import matplotlib.pyplot as plt

plt.plot(x_values, y_values, label='Quadratic B-Spline')
plt.title('Quadratic B-Spline')
plt.xlabel('x')
plt.ylabel('B-Spline value')
plt.legend()
plt.grid(True)
plt.show()
