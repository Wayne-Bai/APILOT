import numpy as np
from scipy.interpolate import griddata

# Example data points (x, y, z)
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
values = np.array([0, 1, 1, 2])

# Grid points to interpolate over
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Interpolate the data
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

# Now grid_z contains the interpolated values over the 2-D grid
