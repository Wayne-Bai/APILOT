
import numpy as np

def compute_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)
