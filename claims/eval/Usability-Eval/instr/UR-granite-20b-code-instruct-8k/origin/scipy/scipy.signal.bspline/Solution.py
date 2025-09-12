import numpy as np
from scipy.interpolate import splrep, splev

def bspline_basis_function(t, n, knots):
    """
    Generate a B-spline basis function of order n.
    
    Parameters
    ----------
    t : array_like
        Points at which to evaluate the basis function.
    n : int
        Order of the basis function.
    knots : array_like
        Knots of the B-spline.
    
    Returns
    -------
    bsplines : array_like
        B-spline basis function evaluated at `t`.
    """
    t = np.array(t)
    knots = np.array(knots)
    bsplines = np.zeros((len(t), len(knots)-n-1))
    for i in range(len(knots)-n-1):
        bsplines[:, i] = splev(t, (knots, np.ones(n+1)*i, n))
    
    return bsplines
