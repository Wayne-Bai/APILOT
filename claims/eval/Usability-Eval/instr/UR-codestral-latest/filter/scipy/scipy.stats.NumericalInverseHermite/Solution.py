import numpy as np
from scipy.interpolate import PchipInterpolator

# Example data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Create interpolators
interp = PchipInterpolator(x, y)

# Use the interpolator
x_new = np.linspace(0, 5, num=50)  # Create new x values
y_new = interp(x_new)  # Get corresponding y values
