import scipy.interpolate as spi
import numpy as np

def approximate_inverse_cdf(x, y, order=3):
    """
    Approximates the inverse of a statistical distribution's CDF using a Hermite spline.
    The function assumes 'x' as values from the CDF and 'y' as the corresponding quantiles.

    :param x: array-like, values from the CDF (e.g., np.linspace(0, 1, num_points))
    :param y: array-like, corresponding quantiles
    :param order: int, order of the Hermite spline
    :return: Hermite spline function that approximates the inverse CDF
    """
    # Create a Hermite spline of specified order
    spline = spi.PchipInterpolator(x, y, extrapolate=True, axis=0)

    return spline

# Example usage:
# Generate sample data (e.g., for a normal distribution)
from scipy.stats import norm

# Sample data for the CDF and the quantiles
num_points = 100
quantiles = np.linspace(0, 1, num_points)
cdf_values = norm.ppf(quantiles)

# Approximate inverse CDF
inverse_cdf_spline = approximate_inverse_cdf(quantiles, cdf_values, order=3)

# Test the resulting function
test_quantiles = np.array([0.05, 0.5, 0.95])
approx_inverse_values = inverse_cdf_spline(test_quantiles)
print("Approximated inverse CDF values:", approx_inverse_values)
