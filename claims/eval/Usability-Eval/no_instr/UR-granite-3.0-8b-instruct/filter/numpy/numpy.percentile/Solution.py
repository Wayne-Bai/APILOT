import numpy as np

def percentile(arr, q, axis=None):
    return np.percentile(arr, q, axis=axis)
