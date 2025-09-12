import numpy as np
from scipy.interpolate import BSpline

def quadratic_bspline(x, knots, coeffs):
    """
    Compute a quadratic B-spline.
    
    Parameters:
    x (array_like): The points at which to evaluate the spline.
    knots (array_like): The knot points.
    coeffs (array_like): The coefficients for the spline.
    
    Returns:
    array_like: The values of the quadratic B-spline at the points x.
    """
    # Ensure the degree is 2 for a quadratic B-spline
    degree = 2
    # Create the B-spline object
    bspline = BSpline(knots, coeffs, degree)
    # Evaluate the spline at the points x
    return bspline(x)

# Example usage:
knots = np.array([0, 0, 0, 1, 2, 3, 4, 4, 4])
coeffs = np.array([0, 1, 2, 3, 4, 5, 6])
x = np.linspace(0, 4, 100)

# Compute the quadratic B-spline
y = quadratic_bspline(x, knots, coeffs)

# Plotting the result (optional)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title('Quadratic B-spline')
plt.show()
