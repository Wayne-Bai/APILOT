import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Sample data points
points = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
values = np.array([1, 2, 3, 4])

# Grid where we want to interpolate data
grid_x, grid_y = np.mgrid[-0.5:1.5:100j, -0.5:1.5:100j]

# Interpolating using griddata
grid_z = griddata(points, values, (grid_x, grid_y), method='linear')

# Plotting the results
plt.imshow(grid_z.T, extent=(-0.5, 1.5, -0.5, 1.5), origin='lower')
plt.plot(points[:, 0], points[:, 1], 'ko', markersize=10)
plt.title('2D Interpolation using Scipy')
plt.colorbar(label='Interpolated values')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
