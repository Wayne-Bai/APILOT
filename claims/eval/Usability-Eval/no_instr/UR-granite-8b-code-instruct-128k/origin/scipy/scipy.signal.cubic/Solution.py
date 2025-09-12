from scipy.interpolate import CubicBSpine

# Define your data here
data = [0, 0, 1, 1, 0, 0, 1, 1]

# Create a cubic B-spline object
bspline = CubicBSpine(data)

# Evaluate the B-spline at a set of points
x = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75]
y = bspline(x)

# Print the results
print(x)
print(y)
