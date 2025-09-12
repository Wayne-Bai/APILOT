import scipy.interpolate

# Define the control points
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 0.2, 0.4, 0.8, 1.3, 2.1, 2.7, 3.2, 3.5, 3.7, 4]

# Create the B-spline
spline = scipy.interpolate.make_interp_spline(x, y, k=2)

# Generate the B-spline values
x_new = [1.5, 2.5, 3.5, 4.5, 5.5]
y_new = spline(x_new)

print(y_new)
