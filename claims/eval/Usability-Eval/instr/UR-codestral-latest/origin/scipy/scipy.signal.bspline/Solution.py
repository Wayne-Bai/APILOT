import numpy as np
import scipy.interpolate as interpolate

def b_spline_basis(knots, n, x):
    # Create a B-spline object
    bspline = interpolate.BSpline(knots, np.identity(len(knots)), n)

    # Evaluate the B-spline basis functions at x
    basis = bspline(x)

    return basis
