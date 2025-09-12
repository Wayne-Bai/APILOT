import numpy as np
from scipy.stats import hmean

def weighted_harmonic_mean(data, weights, axis=0):
    """
    Calculate the weighted harmonic mean along the specified axis.
    
    Parameters:
    data (array-like): Input data for which to calculate the weighted harmonic mean.
    weights (array-like): Weights for the data.
    axis (int): The axis along which to compute the weighted harmonic mean.
    
    Returns:
    ndarray: Weighted harmonic mean of the input data along the specified axis.
    """
    # Convert input data to numpy array
    data = np.asarray(data)
    weights = np.asarray(weights)

    # Calculate the weighted harmonic mean using broadcasting
    weighted_hm = hmean(data / weights, axis=axis) * np.sum(weights, axis=axis) / np.sum(weights / data, axis=axis)
    
    return weighted_hm
