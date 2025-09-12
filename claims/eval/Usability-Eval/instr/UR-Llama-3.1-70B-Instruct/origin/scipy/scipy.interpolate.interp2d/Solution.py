import numpy as np
from scipy.interpolate import griddata

# Define the data points (x, y) and the corresponding values z
x = np.random.rand(100)
y = np.random.rand(100)
z = np.sin(x) + np.cos(y)

# Create a 2-D grid of coordinates
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
Xi, Yi = np.meshgrid(xi, yi)

# Interpolate the values at the grid points
Zi = griddata((x, y), z, (Xi, Yi), method='linear')

# Print the interpolated values
print(Zi)

# Alternatively, you can use the Rbf (radial basis function) interpolator
from scipy.interpolate import Rbf
rbf = Rbf(x, y, z, function='linear')
Zi_rbf = rbf(Xi, Yi)

# Print the interpolated values
print(Zi_rbf)
