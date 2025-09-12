import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

# Create a grid of data points
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2, 3])
z = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 7]])

# Create a grid of interpolated values using griddata
xi = np.linspace(0, 3, 100)
yi = np.linspace(0, 3, 100)
xi, yi = np.meshgrid(xi, yi)

# Use a method like 'linear' or 'cubic' for interpolation
zi = interp.griddata((x.flatten(), y.flatten()), z.flatten(), (xi, yi), method='cubic')

# Plot the original data points and the interpolated surface
plt.figure()
plt.imshow(zi, extent=(0, 3, 0, 3), origin='lower')
plt.scatter(x, y, c='red')  # original data points
plt.colorbar()
plt.title('2D Interpolation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
