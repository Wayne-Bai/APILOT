import numpy as np
import scipy.signal as signal
from scipy.stats import gmean

def weighted_geometric_mean(data, weights):
    gmean_ = signal.gmean(data, weights)
    return gmean_

# Example usage
data = np.array([1, 2, 3, 4])
weights = np.array([0.1, 0.2, 0.3, 0.4])
result = weighted_geometric_mean(data, weights)
print(result)
