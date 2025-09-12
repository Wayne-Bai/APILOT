import numpy as np
from scipy.interpolate import BSpline

def quadratic_bspline(x, knots, coeffs):
    """
    Compute a quadratic B-spline.

    Parameters:
    x (array_like): The points at which to evaluate the spline.
    knots (array_like): The knot points of the spline.
    coeffs (array_like): The coefficients of the spline.

    Returns:
    array_like: The values of the quadratic B-spline at the points x.
    """
    # Ensure the degree is 2 for a quadratic B-spline
    degree = 2
    # Create the B-spline object
    bspline = BSpline(knots, coeffs, degree)
    # Evaluate the B-spline at the points x
    return bspline(x)

# Example usage:
if __name__ == "__main__":
    # Define the knots and coefficients
    knots = np.array([0, 1, 2, 3, 4, 5])
    coeffs = np.array([1, 2, 3, 4, 5])
    x = np.linspace(0, 5, 100)
    
    # Compute the quadratic B-spline
    y = quadratic_bspline(x, knots, coeffs)
    
    # Print the result
    print(y)
