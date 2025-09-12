import numpy as np
from scipy.interpolate import make_interp_spline

# Define the knot vector
knots = [0, 1/3, 2/3, 1]

# Define the control points
control_points = [[0, 0], [1/3, 1], [2/3, -1], [1, 0]]

# Create the B-spline curve
curve = make_interp_spline(knots, control_points)

# Evaluate the curve at a set of points
x = np.linspace(0, 1, 100)
y = curve(x)

# Plot the curve
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
