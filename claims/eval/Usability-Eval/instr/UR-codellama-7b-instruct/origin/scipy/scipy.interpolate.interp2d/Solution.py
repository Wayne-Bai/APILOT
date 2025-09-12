
import numpy as np
from scipy import interpolate

# Define the grid points for the 2-D grid
x = np.linspace(0, 10, 5)
y = np.linspace(0, 10, 5)
X, Y = np.meshgrid(x, y)

# Define the function to be interpolated over the 2-D grid
def func(x, y):
    return x**2 + y**2

# Interpolate over the 2-D grid using nearest-neighbor interpolation
f = interpolate.NearestNDInterpolator((X, Y), func(X, Y))

# Evaluate the interpolated function at a new set of points
new_x = np.linspace(-10, 20, 3)
new_y = np.linspace(-10, 20, 3)
Z = f(new_x, new_y)

# Plot the interpolated function using matplotlib
import matplotlib.pyplot as plt
plt.pcolor(X, Y, Z, cmap='jet')
plt.colorbar()
plt.show()
