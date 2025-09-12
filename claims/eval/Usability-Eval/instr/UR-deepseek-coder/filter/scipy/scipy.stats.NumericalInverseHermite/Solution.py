import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.stats import norm

def approximate_inverse_cdf(dist, order=3, n_points=1000):
    """
    Approximates the inverse of a continuous statistical distribution's CDF
    using a Hermite spline of the specified order.

    Parameters:
    dist: scipy.stats.rv_continuous
        The continuous distribution object.
    order: int, optional
        The order of the Hermite spline. Default is 3.
    n_points: int, optional
        The number of points to use for the approximation. Default is 1000.

    Returns:
    callable: A function that approximates the inverse CDF.
    """
    # Generate points for the CDF
    x = np.linspace(dist.ppf(0.001), dist.ppf(0.999), n_points)
    cdf_values = dist.cdf(x)
    
    # Use PchipInterpolator for Hermite spline interpolation
    inverse_cdf_approx = PchipInterpolator(cdf_values, x, extrapolate=False)
    
    return inverse_cdf_approx

# Example usage with a normal distribution
normal_dist = norm()
inverse_cdf = approximate_inverse_cdf(normal_dist, order=3)

# Test the inverse CDF approximation
p = np.linspace(0.01, 0.99, 100)
inv_values = inverse_cdf(p)

print(inv_values)
