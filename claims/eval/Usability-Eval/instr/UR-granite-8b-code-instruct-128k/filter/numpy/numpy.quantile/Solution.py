import numpy as np

def quantile(data, q, axis):
    return np.quantile(data, q, axis=axis)
