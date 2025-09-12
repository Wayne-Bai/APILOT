
import numpy as np
from scipy.interpolate import BSpline

# Define the knots for a quadratic B-spline
knots = np.array([0, 0, 0, 1, 2, 3, 3, 3])

# Define the degree of the spline
degree = 2

# Create a quadratic B-spline object
quadratic_bspline = BSpline(degree, knots)

# Display the B-spline object
print(quadratic_bspline)
