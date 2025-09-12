import numpy as np
from scipy.interpolate import interp2d

# Define the function to be interpolated
def func(x, y):
    return x**2 + y**2

# Create the x and y coordinates for the grid
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

# Evaluate the function at the grid points
z = func(x, y)

# Interpolate over the grid using cubic interpolation
f = interp2d(x, y, z, kind='cubic')

# Create a new set of x and y coordinates to interpolate at
new_x = np.linspace(-5, 5, 10)
new_y = np.linspace(-5, 5, 10)

# Interpolate the function at the new points
new_z = f(new_x, new_y)

print(new_z)
