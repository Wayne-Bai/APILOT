import numpy as np
from scipy.interpolate import make_interp_spline

def approx_inverse_cdf(cdf, order=5):
    """
    Approximates the inverse of a continuous statistical distribution's CDF
    using a Hermite spline.

    Parameters:
    cdf (function): The continuous statistical distribution's CDF.
    order (int): The order of the Hermite spline. Default is 5.

    Returns:
    function: The approximate inverse CDF as a function of the desired probability.
    """
    # Generate a range of probabilities
    probs = np.linspace(0, 1, 1000)

    # Evaluate the CDF at these probabilities
    cdf_values = cdf(probs)

    # Create a Hermite spline with the specified order
    spline = make_interp_spline(cdf_values, probs, k=order)

    # Define the approximate inverse CDF function
    def inv_cdf(p):
        return spline(p)

    return inv_cdf
