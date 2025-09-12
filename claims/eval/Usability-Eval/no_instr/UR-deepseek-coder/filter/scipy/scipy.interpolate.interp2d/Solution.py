import numpy as np
from scipy.interpolate import griddata

# Example data points and values
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
values = np.array([0, 1, 1, 0])

# Grid points to interpolate over
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]

# Interpolate the data
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

# Display the result
import matplotlib.pyplot as plt
plt.imshow(grid_z.T, extent=(0,1,0,1), origin='lower')
plt.colorbar()
plt.show()
