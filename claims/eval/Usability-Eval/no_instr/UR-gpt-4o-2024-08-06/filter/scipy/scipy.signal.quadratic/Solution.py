import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define knot vector and coefficients for a quadratic B-spline
knots = np.arange(8)  # Knot vector
coefficients = np.random.rand(5)  # Random coefficients for the B-spline
degree = 2  # Quadratic spline

# Create a B-spline representation
b_spline = BSpline(knots, coefficients, degree)

# Evaluation points
x = np.linspace(2, 6, 100)

# Evaluate the B-spline
y = b_spline(x)

# Plot the B-spline
plt.plot(x, y, label='Quadratic B-spline')
plt.title('Quadratic B-Spline')
plt.xlabel('x')
plt.ylabel('B-spline value')
plt.grid(True)
plt.legend()
plt.show()
