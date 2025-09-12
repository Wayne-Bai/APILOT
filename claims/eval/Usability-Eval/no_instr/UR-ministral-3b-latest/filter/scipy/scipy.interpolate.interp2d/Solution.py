import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Create a 2-D grid for interpolation
x = np.linspace(0, 10, 11)
y = np.linspace(0, 10, 11)
xi, yi = np.meshgrid(x, y)

# Create sample data
z = np.sin(np.sqrt(x**2 + y**2))

# Perform interpolation
zi = griddata((x.ravel(), y.ravel()), z.ravel(), (xi, yi), method='cubic')

# Plot the original data and the interpolated data
plt.plot(x, y, 'o', label='Original data')
plt.contourf(x, y, zi, cmap='rainbow', alpha=0.7, levels=100, label='Interpolated data')
plt.legend()
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
