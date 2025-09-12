import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=None):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    
    if not isinstance(weights, np.ndarray):
        weights = np.array(weights)
    
    if data.shape != weights.shape:
        raise ValueError("Shapes of data and weights must match.")
    
    log_data = np.log(data)
    
    weighted_mean_log = np.average(log_data, weights=weights, axis=axis)
    
    weighted_geom_mean = np.exp(weighted_mean_log)
    
    return weighted_geom_mean

# Example usage
data = np.array([[1, 2], [3, 4]])
weights = np.array([[0.25, 0.75], [0.1, 0.9]])
result = weighted_geometric_mean(data, weights, axis=1)
print("Weighted Geometric Mean along axis 1:", result)
