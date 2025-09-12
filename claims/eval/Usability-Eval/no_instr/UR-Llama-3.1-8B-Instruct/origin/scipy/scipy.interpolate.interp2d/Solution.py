import numpy as np
from scipy.interpolate import griddata

# Create a grid of points
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

# Create an array of points where the data will be interpolated
xi = np.linspace(-10, 10, 50)
yi = np.linspace(-10, 10, 50)
Xi, Yi = np.meshgrid(xi, yi)

# Create some data to interpolate over the grid
data = np.sin(np.sqrt(X**2 + Y**2))  # e.g. data from a 2d array
points = np.array([[x, y] for x, y in zip(X.ravel(), Y.ravel())])

# Interpolate the data
interpolated_data = griddata(points, data.ravel(), (Xi, Yi), method='linear')

# Plot the results
import matplotlib.pyplot as plt

plt.contourf(Xi, Yi, interpolated_data)
plt.colorbar(label='Interpolated Data')
plt.show()
