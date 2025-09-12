import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_interp_spline

# Define knots for a quadratic B-spline
knots = [0, 0, 0, 1, 2, 2, 2]  # Example knots
degree = 2  # Quadratic B-spline

# Generate a B-spline basis function
spline = BSpline(knots, np.array([1, 0, 0]), degree)

# Define a range of x values
x = np.linspace(0, 2, 100)

# Evaluate the spline
y = spline(x)

# Plotting the B-spline
plt.plot(x, y, label='Quadratic B-Spline')
plt.title('Quadratic B-Spline Visualization')
plt.xlabel('x')
plt.ylabel('B-Spline value')
plt.legend()
plt.grid()
plt.show()
