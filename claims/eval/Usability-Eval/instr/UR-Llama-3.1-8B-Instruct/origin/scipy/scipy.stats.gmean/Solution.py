import numpy as np
from scipy import stats

# Define a function to compute weighted geometric mean
def weighted_geometric_mean(data, weights, axis):
    """
    Compute the weighted geometric mean along the specified axis.

    Parameters:
    data (numpy array): Input array
    weights (numpy array): Weight array
    axis (int): Axis along which to compute the weighted geometric mean

    Returns:
    weighted_geometric_mean (float): Weighted geometric mean
    """

    # Calculate the weighted log of the data along the specified axis
    weighted_log_data = np.log(data) * weights
    
    # Calculate the weighted sum of the log data along the specified axis
    weighted_sum_log_data = np.sum(weighted_log_data, axis=axis)
    
    # Calculate the weighted geometric mean by exponentiating the weighted sum
    weighted_geometric_mean = np.exp(weighted_sum_log_data / np.sum(weights, axis=axis))
    
    return weighted_geometric_mean

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.5, 0.3, 0.2], [0.7, 0.2, 0.1]])
axis = 0

weighted_geometric_mean_value = weighted_geometric_mean(data, weights, axis)
print("Weighted geometric mean:", weighted_geometric_mean_value)
