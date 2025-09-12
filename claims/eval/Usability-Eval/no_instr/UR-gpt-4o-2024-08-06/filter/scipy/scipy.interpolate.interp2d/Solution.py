import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Define grid points (x, y) for known data
x = np.array([0, 1, 1, 0])
y = np.array([0, 0, 1, 1])
values = np.array([0, 1, 2, 3])

# Define the grid where interpolation is performed
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Perform interpolation
grid_values = griddata((x, y), values, (grid_x, grid_y), method='cubic')

# Plotting the result
plt.imshow(grid_values.T, extent=(0,1,0,1), origin='lower')
plt.scatter(x, y, c=values, edgecolor='k')
plt.colorbar()
plt.title('2D Interpolation using scipy\'s griddata')
plt.show()
