import numpy as np

def compute_quantile(data, q):
    quantile = np.quantile(data, q)
    return quantile
