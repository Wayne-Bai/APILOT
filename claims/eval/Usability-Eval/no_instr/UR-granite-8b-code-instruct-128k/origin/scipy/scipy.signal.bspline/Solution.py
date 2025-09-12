
from scipy.interpolate import BSpline

# Define the knot vector
knots = [0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]

# Define the control points
ctrlpts = [[0, 0], [10, 10], [10, 10], [20, 20], [30, 30], [40, 40], [40, 40], [50, 50]]

# Define the degree of the B-spline
degree = 3

# Create a B-spline basis function
bspline = BSpline(knots, ctrlpts, degree)

# Evaluate the B-spline at a given parameter value
t = 2
result = bspline(t)

# Print the result
print(result)
