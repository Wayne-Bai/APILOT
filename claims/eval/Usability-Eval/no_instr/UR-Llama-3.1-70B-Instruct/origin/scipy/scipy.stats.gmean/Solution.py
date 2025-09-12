import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=0):
    """
    Compute the weighted geometric mean along the specified axis.

    Parameters:
    data (numpy.ndarray): Input data.
    weights (numpy.ndarray): Weights for the data.
    axis (int): Axis along which to compute the geometric mean. Default: 0.

    Returns:
    weighted_gmean (float or numpy.ndarray): Weighted geometric mean along the specified axis.
    """
    # Ensure data and weights have same shape
    if data.shape!= weights.shape:
        raise ValueError("Data and weights must have same shape.")

    # Clip data and weights to prevent division by zero
    data = np.clip(data, a_min=1e-10, a_max=None)
    weights = np.clip(weights, a_min=0, a_max=None)

    # Normalize weights
    sum_weights = np.sum(weights, axis=axis, keepdims=True)
    weights = weights / sum_weights

    # Compute weighted logarithmic sum
    log_data = np.log(data)
    weighted_log_sum = np.sum(log_data * weights, axis=axis)

    # Compute weighted geometric mean
    weighted_gmean = np.exp(weighted_log_sum)

    return weighted_gmean

# Example usage:
if __name__ == "__main__":
    data = np.array([[1, 2, 3], [4, 5, 6]])
    weights = np.array([[0.5, 0.3, 0.2], [0.4, 0.4, 0.2]])
    axis = 0

    weighted_gmean = weighted_geometric_mean(data, weights, axis=axis)
    print("Weighted geometric mean:", weighted_gmean)
