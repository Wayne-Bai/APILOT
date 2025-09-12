import numpy as np
from scipy.interpolate import griddata

# Example 2D data
points = np.random.rand(100, 2)  # random points in 2 dimensions
values = np.sin(points[:, 0]*2*np.pi) * np.cos(points[:, 1]*2*np.pi)  # Sin-Cos function values at these points

# Grid to interpolate on
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]  # Creating a 100x100 grid

# Interpolate data
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')  # 'cubic' interpolation

# grid_z now contains the interpolated values which can be used for further processing or plotting
