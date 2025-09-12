import numpy as np

def compute_quantile(data, q, axis=0):
    data_sorted = np.sort(data, axis=axis)
    index = int(q * (data.shape[axis] - 1))
    return np.take_along_axis(data_sorted, index, axis=axis)
