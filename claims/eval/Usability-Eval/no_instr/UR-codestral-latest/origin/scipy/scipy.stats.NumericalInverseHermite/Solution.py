import numpy as np
import scipy.stats as stats
from scipy.interpolate import UnivariateSpline

def cdf_to_inverse_hermite(dist, order=3, n=1000, **kwargs):
    """
    Approximates the inverse of a continuous statistical distribution’s CDF with a Hermite spline.

    :param dist: a scipy.stats distribution instance
    :param order: the order of the hermite spline
    :param n: number of samples to generate the spline
    :param kwargs: additional arguments for scipy.stats.ppf
    :return: a scipy.interpolate.UnivariateSpline instance
    """
    x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), n)
    y = dist.ppf(np.linspace(0.01, 0.99, n), **kwargs)
    return UnivariateSpline(x, y, k=order, s=0)

# Example usage:
norm_inv = cdf_to_inverse_hermite(stats.norm(), order=3)
