import numpy as np
from scipy.interpolate import make_interp_spline

# Define the order of the B-spline basis function (n)
n = 3

# Create an array of data points for the B-spline basis function
x = np.linspace(0, 1, n + 1)
y = np.sin(2 * np.pi * x)

# Create a spline object from the data points
spline = make_interp_spline(x, y)

# Evaluate the B-spline basis function at a set of query points
query_points = np.linspace(0, 1, 100)
values = spline(query_points)
