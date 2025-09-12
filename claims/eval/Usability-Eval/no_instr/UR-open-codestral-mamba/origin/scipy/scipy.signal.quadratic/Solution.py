import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

# This is equivalent to bspline(x, 2)

# Create some data
x = np.linspace(-15, 15, 70)
y = np.cos(x/2) + np.sin(x/7)

# Create array of x values
xnew = np.linspace(-15, 15, 500)

# Define the interpolation function
spl = make_interp_spline(x, y, k=2)  # BSpline object, k=2, is the same as bspline(x, 2)

# Evaluate the spline at the new x values
ynew = spl(xnew)

# Now you can plot the original data and the interpolated data
import matplotlib.pyplot as plt
plt.figure()
plt.plot(x, y, 'x', label='original points')
plt.plot(xnew, ynew, label='interpolation')
plt.legend()
plt.show()
