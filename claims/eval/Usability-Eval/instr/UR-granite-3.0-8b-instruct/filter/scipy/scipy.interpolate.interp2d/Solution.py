import numpy as np
from scipy.interpolate import interp2d

# Assuming we have a 2D grid of data
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Create an interpolating function
f = interp2d(x, y, Z, kind='cubic')

# Evaluate the interpolating function on a new set of points
xnew = np.linspace(0, 10, 50)
ynew = np.linspace(0, 10, 50)
Znew = f(xnew[:, np.newaxis], ynew[np.newaxis, :])
