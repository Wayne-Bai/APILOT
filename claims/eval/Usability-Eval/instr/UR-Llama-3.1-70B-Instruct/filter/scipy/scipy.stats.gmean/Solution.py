import scipy.stats as stats
import numpy as np

def weighted_geometric_mean(data, weights, axis=0):
    """
    Compute the weighted geometric mean along the specified axis.

    Parameters:
    data (numpy.ndarray): The input data.
    weights (numpy.ndarray): The weights for the data.
    axis (int, optional): The axis along which the weighted geometric mean is calculated. Defaults to 0.

    Returns:
    float: The weighted geometric mean.
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        # Add a small value to data to avoid zero values
        data = np.maximum(data, np.finfo(data.dtype).tiny)
        
        # Calculate the weighted log of the data
        weighted_log_data = (np.log(data) * weights).sum(axis)
        
        # Calculate the sum of the weights
        sum_weights = np.sum(weights, axis)
        
        # Calculate the weighted geometric mean
        weighted_geometric_mean = np.exp(weighted_log_data / sum_weights)
        
        return weighted_geometric_mean


# Example usage:
if __name__ == "__main__":
    data = np.array([[1, 2, 3], [4, 5, 6]])
    weights = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

    print(weighted_geometric_mean(data, weights, axis=0))
    print(weighted_geometric_mean(data, weights, axis=1))
