import numpy as np
def compute_qth_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)
