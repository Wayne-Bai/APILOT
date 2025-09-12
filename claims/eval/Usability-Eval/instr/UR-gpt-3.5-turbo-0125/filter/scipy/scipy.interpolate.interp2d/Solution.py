
import numpy as np
from scipy.interpolate import griddata

# Sample data
points = np.random.rand(100, 2)
values = np.random.rand(100)

# Define grid
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Perform 2D interpolation
interpolated_values = griddata(points, values, (grid_x, grid_y), method='linear')
