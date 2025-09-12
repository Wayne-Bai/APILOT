import numpy as np

def percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)
