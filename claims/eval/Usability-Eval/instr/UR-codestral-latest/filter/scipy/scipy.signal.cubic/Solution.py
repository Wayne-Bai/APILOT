import numpy as np
from scipy.interpolate import make_interp_spline

# Define the x and y values
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 3, 4, 2, 3, 1])

# Create the cubic bspline (i.e., make_interp_spline with k=3)
bspline = make_interp_spline(x, y, k=3)

# Evaluate the bspline for a new set of x values
x_new = np.linspace(min(x), max(x), 300)
y_new = bspline(x_new)
