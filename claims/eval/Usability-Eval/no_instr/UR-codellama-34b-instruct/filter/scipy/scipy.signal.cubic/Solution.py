
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the x coordinates for the cubic B-spline
x = np.array([0, 1, 2, 3])

# Define the y coordinates for the cubic B-spline
y = np.array([0, 1, 4, 9])

# Create a cubic B-spline using make_interp_spline function
bspline = make_interp_spline(x, y)
