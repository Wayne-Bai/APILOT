# Import necessary libraries
import numpy as np
from scipy.interpolate import splev, splrep
import matplotlib.pyplot as plt

# Create a sample dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Create a cubic B-spline (order 3)
spl = splrep(x, y, k=3)

# Generate interpolated x values
x_interp = np.linspace(x[0], x[-1], 100)

# Evaluate the B-spline at interpolated x values
y_interp = splev(x_interp, spl)

# Plot the original data points and the interpolated curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Original data points')
plt.plot(x_interp, y_interp, 'r-', label='Cubic B-spline interpolation')
plt.legend()
plt.show()
