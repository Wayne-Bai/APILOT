import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=0):
    """
    Compute the weighted geometric mean along the specified axis.

    Parameters:
    data (array_like): Input data.
    weights (array_like): Weights corresponding to the data.
    axis (int): Axis along which the mean is computed.

    Returns:
    numpy.ndarray: Weighted geometric mean along the specified axis.
    """
    
    # Convert data and weights to numpy arrays
    data = np.array(data)
    weights = np.array(weights)
    
    # Calculate the weighted geometric mean
    weighted_mean = np.exp(np.sum(weights * np.log(data), axis=axis) / np.sum(weights, axis=axis))
    
    return weighted_mean
