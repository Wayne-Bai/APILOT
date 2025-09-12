from scipy.interpolate import splprep, splev
import numpy as np

# Generate x and y data
x = np.linspace(0, 10, 100)
y = np.sin(np.linspace(0, 10, 100))

# Reshape the data
x, y = np.reshape(x, (-1, 1)), np.reshape(y, (-1, 1))

# Create a cubic spline through the points
knots, cp = splprep([x, y], u=None, s=0.0, per=0, k=3)

# Evaluate the spline at new points
u_new = np.linspace(0, 1, 100)
x_new, y_new = splev(u_new, knots, der=0)

# Plot the original data and the cubic spline
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_new, y_new, label='Cubic spline')
plt.legend()
plt.show()
