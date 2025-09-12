from scipy.special import hermite
import numpy as np
from scipy.interpolate import make_interp_spline

def hermite_spline_cdf(cdf, order):
    x = np.linspace(0, 1, 1000)  # Example: 1000 points between 0 and 1
    y = cdf(x)  # Assuming cdf is a function that takes a single argument x

    # Create a Hermite spline
    spline = make_interp_spline(x, y, k=order, bc_type="natural")

    # Return the inverse of the CDF
    return spline(cdf)
