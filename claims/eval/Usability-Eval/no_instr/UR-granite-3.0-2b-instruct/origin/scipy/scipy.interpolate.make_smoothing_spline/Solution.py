import numpy as np
from scipy.interpolate import CubicSpline

def compute_smoothing_cubic_spline(x, y, lam=None):
    if lam is None:
        # Compute the GCV criteria
        n = len(x)
        sse = np.sum((y - np.interp(x, x, y))**2)
        sst = np.sum((y - np.mean(y))**2)
        lam = sse / (n * sst)

    # Compute the smoothing cubic spline
    cs = CubicSpline(x, y, bc_type='natural', dydx=lam)

    return cs
