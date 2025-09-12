import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Define grid data
x = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
z = np.array([0, 1, 4, 1, 2, 5, 4, 5, 8])

# Define a finer grid for interpolation
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolation using griddata
zi = griddata((x, y), z, (xi, yi), method='cubic')

# Plot the results
plt.figure(figsize=(8, 6))
plt.contourf(xi, yi, zi, levels=15, cmap='viridis')
plt.scatter(x, y, c=z, edgecolor='k', s=100, linewidth=1.5)
plt.colorbar()
plt.title('2D Interpolation using griddata')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
