# Importing the necessary Libraries
from scipy import interpolate
import numpy as np

# Known data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
X, Y = np.meshgrid(x, y)

# Function values at the data points
F = np.array([
    [0.0, 0.1, 0.2, 0.3, 0.4],
    [0.5, 0.6, 0.7, 0.8, 0.9],
    [1.0, 1.1, 1.2, 1.3, 1.4],
    [1.5, 1.6, 1.7, 1.8, 1.9],
    [2.0, 2.1, 2.2, 2.3, 2.4]])

# Defining a rectangular grid, which is defined by a range in x and y
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
Xi, Yi = np.meshgrid(xi, yi)

# Linear interpolation
interp_func = interpolate.interp2d(x, y, F, kind='cubic')
Z = interp_func(xi, yi)
