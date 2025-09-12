import numpy as np
from scipy.interpolate import CubicSpline

def smooth_cubic_spline(x, y, lam=None):
    if lam is None:
        # Compute the GCV criteria to find the optimal lambda
        lambda_opt = 0.0
        for _ in range(100):  # Perform a binary search to find the optimal lambda
            mid = (lambda_opt + 1.0) / 2.0
            spline = CubicSpline(x, y, bc_type='not-a-knot', extrapolate=False, lam=mid)
            residuals = y - spline(x)
            gcv = np.sum(residuals**2) / (len(x) - spline.degrees[0] - 1)
            if gcv < 0.5:
                lambda_opt = mid
            else:
                lambda_opt = 0.0
        lam = lambda_opt

    # Compute the smoothing cubic spline function
    spline = CubicSpline(x, y, bc_type='not-a-knot', extrapolate=False, lam=lam)
    return spline
