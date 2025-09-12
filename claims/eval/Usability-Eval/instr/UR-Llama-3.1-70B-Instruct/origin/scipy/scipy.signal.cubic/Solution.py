import scipy.interpolate as interpolate
import numpy as np

# Generate x and y values for the data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Create a cubic B-spline interpolation function
f = interpolate.interp1d(x, y, kind='cubic')

# Generate new x values for the interpolated curve
x_new = np.linspace(x.min(), x.max(), 300)

# Evaluate the cubic B-spline at the new x values
y_new = f(x_new)

# Print the interpolated y values
print(y_new)
