import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define the knot vector, degree (cubic -> 3), and coefficients
k = 3
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Knot vector
c = [0, 1, 2, 1, 0, 1, 2, 1, 0]        # Coefficients for each basis function

# Create a B-spline object
spline = BSpline(t, c, k)

# Generate x values
x = np.linspace(t[k], t[-k-1], 100)

# Generate the y values (spline values)
y = spline(x)

# Plot the B-spline
plt.plot(x, y, label='Cubic B-spline')
plt.title('Cubic B-spline')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
