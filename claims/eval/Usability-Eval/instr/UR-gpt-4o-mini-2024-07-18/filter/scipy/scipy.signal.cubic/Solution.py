import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_interp_spline

# Define the knots, coefficients, and degree for a cubic B-spline
knots = [0, 0, 0, 1, 2, 3, 3, 3]  # knots must include repeated knots at the boundaries
coefficients = [1, 2, 0, 3]  # coefficients of the B-spline
degree = 3  # Degree of the spline

# Create the cubic B-spline
cubic_bspline = BSpline(knots, coefficients, degree)

# Generate points for plotting
x = np.linspace(0, 3, 100)
y = cubic_bspline(x)

# Plot the B-spline
plt.plot(x, y, label='Cubic B-Spline')
plt.title('Cubic B-Spline')
plt.legend()
plt.grid()
plt.show()
