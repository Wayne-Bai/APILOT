import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
z = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]])

# Define grid
xi = np.linspace(1, 5, 100)
yi = np.linspace(1, 5, 100)

# Interpolate over a 2-D grid
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

# Plot results
plt.imshow(zi, extent=(1, 5, 1, 5))
plt.colorbar()
plt.show()
