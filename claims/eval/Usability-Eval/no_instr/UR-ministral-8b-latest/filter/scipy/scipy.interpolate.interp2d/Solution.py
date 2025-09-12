import numpy as np
from scipy import interpolate

# Example 2D data grid
x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)
x, y = np.meshgrid(x, y)
data = np.sin(x) * np.cos(y)

# Create grid for interpolation
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Perform the interpolation
zi = interpolate.griddata((x.ravel(), y.ravel()), data.ravel(), (xi, yi), method='linear')

# Output the interpolated data grid
print(zi)
