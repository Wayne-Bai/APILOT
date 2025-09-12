from scipy import interpolate
import numpy as np

def generate_bspline_basis(t, n, knots):
    """
    Generate a B-spline basis function of order n.

    Parameters:
    t (float or array-like): time values or array of time values.
    n (int): order of the B-spline.
    knots (array-like): array of knot points.

    Returns:
    ndarray: B-spline basis function values.
    """
    t = np.atleast_1d(t)  # ensure t is an array-like object
    basis = np.zeros((len(t), len(knots) - n - 1))

    for i in range(len(knots) - n - 1):
        if n == 0:
            indicator = (t >= knots[i]) & (t < knots[i+1])
            basis[indicator, i] = 1.0
        else:
            DEN1 = knots[i+n] - knots[i]
            DEN2 = knots[i+n+1] - knots[i+1]
            N1 = ((t - knots[i])/DEN1)*generate_bspline_basis(t, n-1, knots)[:,-n:] if DEN1 != 0 else np.zeros(basis[indicator, i].shape)
            N2 = ((knots[i+n+1]-t)/DEN2)*generate_bspline_basis(t, n-1, knots)[:,-n:] if DEN2 != 0 else np.zeros(basis[indicator, i].shape)

            basis[:,i] = (N1 + N2)[:, i]

    return basis

# Usage example
t = np.linspace(0, 1, 100)
n = 3
knots = np.array([0, 0, 0, 1, 2, 2, 2])
basis = generate_bspline_basis(t, n, knots)
