import numpy as np
from scipy.interpolate import PPoly
from scipy.special import erfinv

def cdf_inv_approx(dist_cdf, x_values, order=3):
    """
    Approximate the inverse of a continuous statistical distribution's CDF 
    using a Hermite spline.

    Parameters
    ----------
    dist_cdf : callable
        The cumulative distribution function (CDF) of the distribution.
    x_values : array-like
        The x-values at which to evaluate the CDF.
    order : int, optional
        The order of the Hermite spline. Defaults to 3.

    Returns
    -------
    pp : PPoly
        The Hermite spline approximation of the inverse CDF.

    Notes
    -----
    This function uses a Hermite spline to approximate the inverse of the CDF,
    which is more accurate than a simple polynomial spline, especially in the 
    tails of the distribution.
    """

    # Evaluate the CDF at the x-values
    y_values = np.array([dist_cdf(x) for x in x_values])

    # Calculate the derivatives of the CDF (up to the specified order)
    dy_values = []
    for i in range(order):
        dy_values.append(np.gradient(y_values, x_values, edge_order=2))

    # Create the Hermite spline
    pp = PPoly.from_spline(x_values, y_values, dy_values, axis=0)

    # Define the inverse CDF function using the Hermite spline
    def inv_cdf(y):
        return pp(y)

    return inv_cdf

# Example usage with the standard normal distribution
def std_norm_cdf(x):
    return (1 + erfinv(2 * x - 1)) / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

x_values = np.linspace(-3, 3, 100)
inv_cdf_approx = cdf_inv_approx(std_norm_cdf, x_values, order=5)

# Test the approximation
y_values = np.linspace(0.001, 0.999, 100)
print(inv_cdf_approx(y_values))
