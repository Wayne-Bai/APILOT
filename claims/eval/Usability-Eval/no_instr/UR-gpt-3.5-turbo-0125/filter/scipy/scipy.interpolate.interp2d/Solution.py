
import numpy as np
from scipy.interpolate import griddata

# Create 2-D grid points (x, y) and corresponding values z
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
z = np.array([1, 4, 9, 16, 25])

# Define the grid to interpolate over
xi = np.linspace(0, 4, 20)
yi = np.linspace(0, 4, 20)
xi, yi = np.meshgrid(xi, yi)

# Interpolate the values over the grid
zi = griddata((x, y), z, (xi, yi), method='cubic')

print(zi)
