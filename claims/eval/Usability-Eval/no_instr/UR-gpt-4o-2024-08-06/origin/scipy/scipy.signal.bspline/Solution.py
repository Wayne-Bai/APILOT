import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define the order of the B-spline
order = 3  # cubic B-spline for example
knots = np.array([0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4])  # Clamped knots
coefficients = np.array([1, 2, 3, 4, 3, 2, 1])  # Example control points

# Create B-spline basis function
b_spline = BSpline(knots, coefficients, order)

# Define the range to evaluate the B-spline
x = np.linspace(0, 4, 100)

# Evaluate the B-spline
y = b_spline(x)

# Plot the B-spline
plt.plot(x, y, label='B-spline')
plt.title('B-spline basis function of order {}'.format(order))
plt.xlabel('x')
plt.ylabel('B-spline value')
plt.grid(True)
plt.legend()
plt.show()
