import numpy as np
from scipy.stats import gmean

def weighted_geometric_mean(data, weights, axis=-1):
    return gmean(data, weights=weights, axis=axis)
