import numpy as np

def calculate_quantile(data, axis=0, q=0.5):
    return np.percentile(data, (q * 100), axis=axis)
