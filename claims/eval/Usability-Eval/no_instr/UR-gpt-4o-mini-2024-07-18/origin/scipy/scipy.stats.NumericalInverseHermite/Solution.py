import numpy as np
from scipy.interpolate import PPoly

def hermite_spline_inverse_cdf(cdf_values, order=3):
    """
    Approximate the inverse of a continuous statistical distribution's CDF
    using a Hermite spline.

    Parameters:
    cdf_values : array_like
        Values of the CDF at specific quantile points.
    order : int
        The order of the Hermite spline.

    Returns:
    func : callable
        A function that approximates the inverse CDF.
    """
    
    n = len(cdf_values)
    if n < order + 1:
        raise ValueError("Insufficient number of CDF values for the specified order.")

    # Generate the knots uniformly
    x = np.linspace(0, 1, n)
    
    # Calculate the first derivative using finite differences
    derivatives = np.gradient(cdf_values, x)

    # Create the spline coefficients
    coeffs = np.zeros((order + 1, n))
    coeffs[0, :] = cdf_values
    coeffs[1, :] = derivatives

    # Create a Hermite spline representation
    spline = PPoly(coeffs, x)

    # Define the inverse CDF function
    def inverse_cdf(p):
        return spline.interpolate(p)

    return inverse_cdf
