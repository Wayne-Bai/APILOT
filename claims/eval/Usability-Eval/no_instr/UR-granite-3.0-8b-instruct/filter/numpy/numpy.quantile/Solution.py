import numpy as np

def compute_q_quantile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)
