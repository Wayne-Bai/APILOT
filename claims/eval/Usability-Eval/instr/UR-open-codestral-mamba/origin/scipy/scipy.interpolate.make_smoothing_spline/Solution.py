from scipy.interpolate import make_interp_spline
import numpy as np

def compute_smoothing_cubic_spline(x, y, lam=None):
    # Compute the number of knots for smoothing spline
    knots = (np.linspace(0, 1, 20))[1:-1]

    # Making a polynomial spline model for the data points
    spline = make_interp_spline(x, y, k=3, t=knots)

    if lam is None:
        # Compute the GCV score for optimal smoothing parameter
        results = spline.gcv()
        lam = results.x

    # Compute the smoothing spline with the optimal (or given) lam
    smoothed_spline = make_interp_spline(x, y, k=3, t=knots, s=lam)

    return smoothed_spline
