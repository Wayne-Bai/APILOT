import numpy as np

def weighted_geometric_mean(data, weights, axis=0):
    """
    Compute the weighted geometric mean along the specified axis.
    """
    log_data = np.log(data)
    log_gmean = np.sum(weights * log_data, axis=axis) / np.sum(weights, axis=axis)
    gmean = np.exp(log_gmean)
    return gmean
