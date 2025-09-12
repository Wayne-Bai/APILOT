import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.stats import norm

def approximate_inverse_cdf(dist, order=3, n_points=1000):
    """
    Approximates the inverse of a continuous statistical distribution's CDF
    using a Hermite spline of the specified order.

    Parameters:
    dist: scipy.stats distribution object
        The distribution whose inverse CDF is to be approximated.
    order: int, optional
        The order of the Hermite spline. Default is 3.
    n_points: int, optional
        Number of points to use for the approximation. Default is 1000.

    Returns:
    callable: A function that approximates the inverse CDF.
    """
    # Generate points for the CDF
    p = np.linspace(0, 1, n_points)
    x = dist.ppf(p)

    # Use PchipInterpolator for Hermite spline interpolation
    interpolator = PchipInterpolator(p, x)

    def inverse_cdf(q):
        return interpolator(q)

    return inverse_cdf

# Example usage with a normal distribution
dist = norm()
inverse_cdf = approximate_inverse_cdf(dist, order=3)

# Test the inverse CDF approximation
test_quantiles = np.linspace(0.01, 0.99, 10)
approximated_values = inverse_cdf(test_quantiles)
print("Approximated inverse CDF values:", approximated_values)
