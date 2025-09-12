import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.stats import norm

def approximate_inverse_cdf_spline(distribution_cdf, num_points=100, order=3):
    # Generate x values and corresponding y values using the distribution's CDF
    x = np.linspace(0, 1, num_points)
    y = distribution_cdf(x)

    # Compute derivatives at each point
    dydx = np.gradient(y, x)

    # Create the Hermite spline
    spline = CubicHermiteSpline(x, y, dydx)

    return spline

# Example usage:
# Normal distribution CDF
normal_cdf = norm.cdf

# Approximate the inverse CDF with Hermite spline of order 3
inverse_cdf_spline = approximate_inverse_cdf_spline(normal_cdf, order=3)

# Evaluate the spline at some point
print(inverse_cdf_spline(.5))
