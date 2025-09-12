import numpy as np
from scipy.interpolate import griddata

# Create a 2-D grid of points
n_points = 100
x = np.linspace(0, 10, n_points)
y = np.linspace(0, 5, n_points)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Interpolate over the grid using griddata
xi = np.linspace(0, 10, 1000)
yi = np.linspace(0, 5, 1000)
Zi = griddata((X, Y), Z, (xi[None,:], yi[:,None]), method='cubic')

# Plot the original data and the interpolated data
import matplotlib.pyplot as plt
plt.pcolor(X, Y, Z, cmap='coolwarm')
plt.colorbar()
plt.contour(xi, yi, Zi, colors='k', linewidths=0.5)
plt.show()
