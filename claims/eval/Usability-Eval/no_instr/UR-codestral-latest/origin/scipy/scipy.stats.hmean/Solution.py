import numpy as np
import scipy.stats as stats

def weighted_hmean(a, weights):
    return len(a) / np.sum(weights / a)

# Test the function
a = np.array([1, 2, 3])
weights = np.array([0.5, 0.3, 0.2])
print(weighted_hmean(a, weights))
