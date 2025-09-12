import numpy as np
from scipy.stats import gmean

def weighted_harmonic_mean(arr, weights):
    """
    Calculate the weighted harmonic mean along the specified axis.

    Parameters:
    arr (numpy.ndarray): Input array.
    weights (numpy.ndarray): Weights for each element in the input array.

    Returns:
    numpy.ndarray: Weighted harmonic mean along the specified axis.
    """
    # Check if the input array and weights have the same shape
    if arr.shape != weights.shape:
        raise ValueError("Input array and weights must have the same shape.")

    # Calculate the weighted harmonic mean along the specified axis
    weighted_harmonic_mean = gmean(arr, axis=0, weights=weights)

    return weighted_harmonic_mean
