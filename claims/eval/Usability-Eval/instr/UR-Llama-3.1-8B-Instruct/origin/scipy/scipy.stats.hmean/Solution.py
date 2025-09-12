import numpy as np
from scipy.stats import gmean

def weighted_harmonic_mean(values, weights, axis=0):
    """
    Calculate the weighted harmonic mean along the specified axis.

    Parameters:
    values (array_like): Input array.
    weights (array_like): Weights array.
    axis (int, optional): Axis along which the mean is computed. Default is 0.

    Returns:
    wm (float): Weighted harmonic mean.
    """
    weighted_values = values / weights
    return gmean(weighted_values, weights=weights, axis=axis)

# Example usage:
values = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.1, 0.2, 0.7], [0.3, 0.4, 0.3]])

wm = weighted_harmonic_mean(values, weights)
print("Weighted harmonic mean:", wm)

wm_axis = weighted_harmonic_mean(values, weights, axis=1)
print("Weighted harmonic mean along axis=1:", wm_axis)
