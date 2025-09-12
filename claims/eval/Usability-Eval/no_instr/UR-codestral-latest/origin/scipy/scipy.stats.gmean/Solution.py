import numpy as np
from scipy import stats

def weighted_geometric_mean(data, weights):
    """
    Calculate the weighted geometric mean of data.

    Parameters
    ----------
    data : numpy array
    weights : numpy array

    Returns
    -------
    weighted geometric mean : float
    """

    # Compute the logarithm of data
    log_data = np.log(data)

    # Compute the weighted sum of logarithms
    weighted_sum = np.sum(weights * log_data) / np.sum(weights)

    # Compute the exponent of the weighted sum of logarithms
    wgm = np.exp(weighted_sum)

    return wgm
