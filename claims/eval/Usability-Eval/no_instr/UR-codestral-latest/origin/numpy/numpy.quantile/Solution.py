import numpy as np

def compute_quantile(data, q, axis=None):
    return np.percentile(data, q*100, axis=axis)
