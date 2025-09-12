
import numpy as np
from scipy.interpolate import BSplineBasis

# Define the number of basis functions (order) and the domain of interpolation
n = 3
xmin = -1
xmax = 1

# Create an instance of BSplineBasis with the desired order and domain
basis = BSplineBasis(n, xmin, xmax)

# Compute the basis functions at a set of points
x = np.linspace(xmin, xmax, 1000)
y = basis.evall(x)

# Plot the basis functions and their derivatives
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
