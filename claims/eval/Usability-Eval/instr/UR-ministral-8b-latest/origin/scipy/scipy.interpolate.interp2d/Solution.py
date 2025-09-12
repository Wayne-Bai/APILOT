import numpy as np
from scipy.interpolate import griddata, RectBivariateSpline

# Create a 2-D grid
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Create some random data
Z = np.sin(np.sqrt(X**2 + Y**2))

# Interpolate over the grid using RectBivariateSpline
interpolator = RectBivariateSpline(x, y, Z)
Z_interp = interpolator(np.linspace(0, 10, 50), np.linspace(0, 10, 50))

# Alternatively, you can use griddata for a multi-dimensional grid
Z1 = interpolator(np.linspace(0, 10, 50), np.linspace(0, 10, 50))

# Compare the interpolated data
print(Z_interp)
