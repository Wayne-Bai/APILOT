import numpy as np
from scipy.interpolate import make_interp_spline

# Define the order of the spline (n)
n = 3

# Create a set of knots for the spline
knots = np.linspace(0, 1, n + 1)

# Create the B-spline basis function
basis_function = make_interp_spline(knots, n)

# Evaluate the basis function at a set of points
x = np.linspace(0, 1, 10)
y = basis_function(x)
