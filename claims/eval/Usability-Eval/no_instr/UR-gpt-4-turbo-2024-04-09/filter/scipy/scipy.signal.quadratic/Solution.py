import numpy as np
from scipy.interpolate import BSpline

# Parameters for the B-spline
knots = np.array([0, 0, 0, 1, 2, 3, 3, 3])  # Ensure there are sufficient knots for quadratic B-spline
degree = 2  # Degree for quadratic B-spline

# Coefficients for the B-spline
# Length should be equal to the number of knots - degree - 1
coefficients = np.array([1, 2, 3, 4])  # Example coefficients

# Create a quadratic B-spline
quadratic_bspline = BSpline(knots, coefficients, degree)

# Example x-values to evaluate the B-spline
x_values = np.linspace(0, 3, 100)

# Evaluate B-spline at the x-values
y_values = quadratic_bspline(x_values)

# Optionally, you can plot the spline curve
import matplotlib.pyplot as plt

plt.plot(x_values, y_values, label='Quadratic B-spline')
plt.title('Quadratic B-spline Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
