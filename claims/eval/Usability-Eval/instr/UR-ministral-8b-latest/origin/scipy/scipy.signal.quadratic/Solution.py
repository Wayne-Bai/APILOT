import numpy as np
import scipy.interpolate as spi

def quadratic_bsp(x, y):
    # Define the knots
    knot_sequence = [0, 1, 2]

    # Create the B-spline object
    b_spline = spi.BSpline(knot_sequence, y, knot=knot_sequence)

    # Define the B-spline of degree 2
    quad_bsp = b_spline.splrep(x, y, s=0)

    return quad_bsp

# Example usage:
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2, 3])
quad_bsp = quadratic_bsp(x, y)

# Interpolate a new set of points
x_new = np.linspace(0, 2, 50)
y_new = spi.splev(x_new, quad_bsp)

import matplotlib.pyplot as plt

plt.plot(x_new, y_new)
plt.plot(x, y, 'ro')
plt.show()
