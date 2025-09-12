import numpy as np
from scipy.interpolate import BSpline

# Define the interval and the number of knots
knots = np.linspace(0, 1, 5)

# Define the coefficients
coefficients = np.random.rand(len(knots)-2)

# Create a B-spline of degree 2
bspline = BSpline(knots, coefficients, 2)

# Now you can use this bspline to evaluate the quadratic B-spline function at specific points
x = np.linspace(0, 1, 100)
y = bspline(x)
