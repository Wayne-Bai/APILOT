import numpy as np
from scipy.interpolate import griddata

# Assuming we have some 2D data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
z = np.array([1, 8, 27, 64, 125])

# Create a 2D grid
xi, yi = np.meshgrid(np.linspace(0, 4, 10), np.linspace(0, 9, 10))

# Interpolate the data onto the grid
zi = griddata((x, y), z, (xi, yi), method='cubic')
