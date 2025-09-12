import numpy as np
from scipy.interpolate import BSpline

def cubic_bspline(x):
    # Define the knots and coefficients for a cubic B-spline
    knots = np.array([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
    coefficients = np.array([0, 0, 0, 1, 0, 0, 0])
    
    # Create the cubic B-spline
    bspline = BSpline(knots, coefficients, 3)
    
    # Evaluate the B-spline at the given points
    return bspline(x)

# Example usage
x_values = np.linspace(-1.5, 1.5, 100)
y_values = cubic_bspline(x_values)

# Plotting the B-spline (optional)
import matplotlib.pyplot as plt
plt.plot(x_values, y_values)
plt.title("Cubic B-spline")
plt.show()
