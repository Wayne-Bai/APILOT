import numpy as np

def percentile(data, q, axis=0):
    return np.percentile(data, q, axis=axis)