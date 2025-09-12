# Import necessary packages
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Create a 2-D grid of points
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Create a 2-D grid of values
values = np.array([[1., 2.], [3., 4.]])

# Create a new 2-D grid of points where we want to interpolate
xi = np.arange(0, 2, 0.01)
yi = np.arange(0, 2, 0.01)
Xi, Yi = np.meshgrid(xi, yi)

# Perform interpolation
zi = griddata(points, values.flatten(), (Xi, Yi), method='nearest')

# Plot the results
plt.contourf(Xi, Yi, zi, levels=100)
plt.colorbar(label='Interpolated Values')
plt.scatter(points[:, 0], points[:, 1], label='Points')
plt.scatter(Xi.flatten(), Yi.flatten(), c='r', s=5, label='Grid Points')
plt.legend()
plt.show()
