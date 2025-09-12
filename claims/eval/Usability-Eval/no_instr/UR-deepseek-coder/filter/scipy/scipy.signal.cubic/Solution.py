import numpy as np
from scipy.interpolate import BSpline

def cubic_bspline(x, knots, coeffs):
    # Ensure the degree is 3 for a cubic B-spline
    degree = 3
    # Create the B-spline object
    spline = BSpline(knots, coeffs, degree)
    # Evaluate the B-spline at the given points
    return spline(x)

# Example usage:
# Define the knots and coefficients for the B-spline
knots = np.array([0, 1, 2, 3, 4, 5])
coeffs = np.array([0, 1, 2, 3, 4])

# Points at which to evaluate the B-spline
x = np.linspace(0, 5, 100)

# Compute the cubic B-spline values
y = cubic_bspline(x, knots, coeffs)

# Plotting the results (optional)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title('Cubic B-spline')
plt.show()
