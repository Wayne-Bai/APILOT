import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Example data
points = np.random.rand(100, 2) * 4 - 2  # 100 points in 2D
values = np.sin(points[:, 0]) * np.cos(points[:, 1])  # Example function

# Grid on which to interpolate
grid_x, grid_y = np.mgrid[-2:2:100j, -2:2:100j]

# Interpolate using linear, cubic and nearest methods
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

# Plotting the results
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(grid_z0.T, extent=(-2, 2, -2, 2), origin='lower')
plt.title('Nearest interpolation')
plt.colorbar()

plt.subplot(132)
plt.imshow(grid_z1.T, extent=(-2, 2, -2, 2), origin='lower')
plt.title('Linear interpolation')
plt.colorbar()

plt.subplot(133)
plt.imshow(grid_z2.T, extent=(-2, 2, -2, 2), origin='lower')
plt.title('Cubic interpolation')
plt.colorbar()

plt.tight_layout()
plt.show()
