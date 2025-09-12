
from scipy import optimize
import numpy as np

def compute_smoothing_cubic_spline(x, y, lam=None):
    """
    Compute the coefficients of a smoothing cubic spline function using the L2 regularization parameter `lam`.

    Args:
        x (array-like): The input array.
        y (array-like): The output array.
        lam (float, optional): The L2 regularization parameter. If None, use the GCV criteria to find it.

    Returns:
        coeffs (array-like): The coefficients of the smoothing cubic spline function.
    """
    # Initialize the coefficients as all 0
    coeffs = np.zeros((4,))

    if lam is None:
        # Use GCV criteria to find the optimal L2 regularization parameter
        lam = optimize.golden_section_search(func=compute_smoothing_cubic_spline, x0=[], args=(x, y), bounds=([0, 1],))

    # Compute the coefficients using the chosen L2 regularization parameter
    for i in range(3):
        coeffs[i] = (np.sum((y - np.dot(np.power(x, i + 4), coeffs[:i]))**2) / (i + 4) + lam * np.linalg.norm(coeffs[:i], 1))
        coeffs[i + 1] = (y - np.dot(np.power(x, i + 4), coeffs[:i])) / (i + 5)
    return coeffs
