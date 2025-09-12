# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splprep

# Function to calculate B-spline basis
def bspline_basis(x, t, k, i):
    if k == 0:
        if t[i] <= x < t[i+1]:
            return 1.0
        else:
            return 0.0
    else:
        denom1 = t[i+k] - t[i]
        term1 = 0.0
        if denom1 > 0.0:
            term1 = ((x-t[i]) / denom1) * bspline_basis(x, t, k-1, i)

        denom2 = t[i+k+1] - t[i+1]
        term2 = 0.0
        if denom2 > 0.0:
            term2 = ((t[i+k+1]-x) / denom2) * bspline_basis(x, t, k-1, i+1)

        return term1 + term2

# Define the knots
t = np.array([0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1])

# Define the order
n = 3

# Generate evaluation points
x = np.linspace(0, 1, 100)

# Calculate B-spline basis
basis = []
for i in range(len(t)-n-1):
    basis.append([bspline_basis(xi, t, n, i) for xi in x])

# Plot the basis
for bi in basis:
    plt.plot(x, bi)

plt.xlabel('x')
plt.ylabel('B-Spline Basis')
plt.show()
