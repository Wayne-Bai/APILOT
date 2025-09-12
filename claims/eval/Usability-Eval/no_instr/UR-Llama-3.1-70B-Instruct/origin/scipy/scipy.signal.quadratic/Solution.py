import numpy as np
from scipy.interpolate import splev, splrep
import matplotlib.pyplot as plt

# Define the x values
x = np.array([1, 2, 3, 4, 5])

# Define the corresponding y values
y = np.array([2, 3, 5, 7, 11])

# Calculate the spline coefficients (k=2 is for quadratic B-spline)
tck = splrep(x, y, k=2)

# Generate x values for plotting
x_smooth = np.linspace(x.min(), x.max(), 100)

# Evaluate the quadratic B-spline at x_smooth values
y_smooth = splev(x_smooth, tck)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Original data points')
plt.plot(x_smooth, y_smooth, label='Quadratic B-spline')
plt.legend()
plt.show()
