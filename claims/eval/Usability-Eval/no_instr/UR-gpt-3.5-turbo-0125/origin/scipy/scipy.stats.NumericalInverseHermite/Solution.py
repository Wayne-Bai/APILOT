
import numpy as np
from scipy.interpolate import HermiteSpline
from scipy.stats import norm

def inverse_cdf_spline(order, dist, num_points):
    x = np.linspace(0, 1, num_points)
    y = dist.ppf(x)
    
    cdf = dist.cdf(y)
    im = np.argsort(cdf)
    return HermiteSpline(cdf[im], y[im], order=order)

# Example usage
order = 3
dist = norm()
num_points = 100
spline = inverse_cdf_spline(order, dist, num_points)
