import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=0):
    # Ensure data and weights are numpy arrays
    data = np.array(data)
    weights = np.array(weights)
    
    # Calculate logarithm of the data
    weighted_log_data = np.log(data) * weights
    
    # Calculate the sum of weights along the specified axis
    sum_of_weights = np.sum(weights, axis=axis)
    
    # Calculate the weighted sum of log data along the specified axis
    weighted_sum_log = np.sum(weighted_log_data, axis=axis)
    
    # Calculate the weighted geometric mean
    geom_mean = np.exp(weighted_sum_log / sum_of_weights)
    
    return geom_mean

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.2, 0.3, 0.5], [0.1, 0.4, 0.5]])
axis = 1

result = weighted_geometric_mean(data, weights, axis)
print("Weighted geometric mean:", result)
