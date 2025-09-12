import scipy.interpolate as si
import numpy as np

# Generate some data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 2, 3, 2, 8, 5, 6, 9, 2, 4])

# Define a quadratic B-spline
bspl = si.CubicSpline(x, y, bc_type='clamped')

# Now, bspl(x) will return the interpolated values
interpolated_y = bspl(x)

# You can also define and use a quadratic B-spline like this:
bspl_quad = si.splrep(x, y, k=2)
interpolated_y_quad = si.splev(x, bspl_quad)
