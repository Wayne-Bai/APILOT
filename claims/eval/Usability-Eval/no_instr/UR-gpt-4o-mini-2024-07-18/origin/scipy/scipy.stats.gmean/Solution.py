import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis):
    """
    Compute the weighted geometric mean along the specified axis.

    Parameters:
    data : array_like
        Input data.
    weights : array_like
        Weights for the data.
    axis : int
        Axis along which to compute the weighted geometric mean.

    Returns:
    result : ndarray
        Weighted geometric mean along the specified axis.
    """
    # Ensure the data and weights are numpy arrays
    data = np.asarray(data)
    weights = np.asarray(weights)

    # Apply the weights by exponentiating them and multiplying by the data
    weighted_data = data ** weights

    # Compute the geometric mean along the specified axis
    gmean_result = gmean(weighted_data, axis=axis)

    # Adjust the result by taking the exp of the mean of the weights along the same axis
    result = np.exp(np.mean(np.log(gmean_result), axis=axis))

    return result
