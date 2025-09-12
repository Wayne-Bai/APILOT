import scipy.stats
import numpy as np
from scipy.interpolate import PchipInterpolator

def approximate_inverse_cdf(distribution, order=3, num_points=100, domain=None):
    """
    Approximate the inverse CDF of a given continuous statistical distribution using a Hermite spline interpolation.

    Parameters:
    - distribution (scipy.stats.rv_continuous): A scipy continuous statistical distribution.
    - order (int): Order of the Hermite spline (PCHIP), by default third order.
    - num_points (int): Number of points to sample from the distribution's CDF.
    - domain (tuple): The lower and upper bounds as a tuple (lower_bound, upper_bound) for sampling the distribution.
                      If None, defaults will be distribution's a (lower) and b (upper) properties.
    
    Returns:
    - PchipInterpolator: A piecewise cubic hermite interpolating polynomial (PCHIP) of the specified order.
    """

    # Use distribution's domain if not provided
    if domain is None:
        domain = (distribution.a, distribution.b)

    # Sampling points in the distribution
    x = np.linspace(domain[0], domain[1], num_points)
    
    # Calculate the CDF at these points
    cdf = distribution.cdf(x)
    
    # Ensure uniqueness for stability in interpolation
    unique_cdf, unique_x = np.unique(cdf, return_index=True)
    x_unique = x[unique_x]

    # Handle edge cases at bounds explicitly to avoid extrapolation issues
    if unique_cdf[0] > 0.001:
        x_unique = np.insert(x_unique, 0, domain[0])
        unique_cdf = np.insert(unique_cdf, 0, 0)
    if unique_cdf[-1] < 0.999:
        x_unique = np.append(x_unique, domain[1])
        unique_cdf = np.append(unique_cdf, 1)
    
    # Create a PCHIP interpolator for the inverse CDF
    inv_cdf = PchipInterpolator(unique_cdf, x_unique)
    
    return inv_cdf
