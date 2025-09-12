from scipy.stats import norm
from scipy.interpolate import make_interp_spline
import numpy as np

# Function to approximate the inverse of a continuous statistical distribution's CDF with a Hermite spline
def hermite_spline(data, order=3):
    x = np.sort(data)
    cdf = np.arange(1, len(x) + 1) / len(x)

    # Interpolation
    interp_spline = make_interp_spline(x, cdf, k=order)

    # Approximate inverse
    inv_spline = lambda y: interp_spline.solve(y - cdf)

    return inv_spline
