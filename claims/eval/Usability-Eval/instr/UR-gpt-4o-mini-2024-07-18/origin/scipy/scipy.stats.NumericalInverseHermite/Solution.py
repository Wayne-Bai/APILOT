import numpy as np
from scipy.interpolate import CubicHermiteSpline

def inverse_cdf_hermite(cdf_values, order=3):
    if order != 3:
        raise ValueError("Currently, only a cubic Hermite spline (order=3) is supported.")

    # Generate x values for the CDF
    x_values = np.linspace(0, 1, len(cdf_values))

    # Calculate the derivatives (slopes) for the CDF
    # Using finite differences as approximations of the derivative
    derivatives = np.gradient(cdf_values, x_values)

    # Create the Hermite spline
    spline = CubicHermiteSpline(x_values, cdf_values, derivatives)

    return spline
