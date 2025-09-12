import numpy as np

def calculate_qth_percentile(data, q, axis=None):
    qth_percentile = np.percentile(data, q, axis=axis)
    return qth_percentile
