import numpy as np
from scipy.interpolate import BSpline

def cubic_b_spline_curve(knots, control_points):
    # Number of knots, suppose we have the same number of control points as knots minus 1
    n_knots = len(knots)

    # Create cubic B-spline curve
    spline = BSpline(control_points[:-1], knots, BCLeft=1, BCRight=1)  # BCLeft, BCRight = 1 for natural spline

    # Generate x values from the start of the domain to the end of the domain
    x = np.linspace(n_knots-2, n_knots-2, num=100)  # Adjust the number of points as needed

    # Evaluate the spline at the x values
    y = spline(x)

    return x, y

# Define knots and control points
knots = [0, 0, 1, 1, 2, 2]
control_points = [0, 1, 1, 0]

# Get the cubic B-spline curve data
x, y = cubic_b_spline_curve(knots, control_points)

# Print the x and y values
print("x:", x)
print("y:", y)
