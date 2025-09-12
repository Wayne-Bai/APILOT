import scipy.interpolate as spi
import numpy as np

def B_spline_basis(n, t, i, x):
    """
    Calculate the B-spline basis function of order n at a given point x.

    Parameters:
    n : int
        The order of the B-spline.
    t : array-like
        The knot sequence.
    i : int
        The index of the ith B-spline.
    x : array-like
        The points where the B-spline is to be evaluated.

    Returns:
    N_i : array-like
        The values of the ith B-spline at each point x.
    """
    # Create a B-spline basis for the given knots and order
    tck = [t, np.eye(len(t))[:,i], n]
    # Calculate the B-spline at each point
    N_i = spi.splev(x, tck)
    return N_i

# Test the function
n = 3
t = [0, 1, 2, 3, 4, 5, 6, 7, 8]
i = 3
x = np.linspace(0, 8, 200)
N_i = B_spline_basis(n, t, i, x)
print(N_i)
