import numpy as np

def compute_qth_quantile(data, q, axis=None):
    if axis is None:
        return np.percentile(np.ravel(data), q)
    elif axis < 0:
        axis = data.ndim + axis
    else:
        axis = int(axis)
    N = data.shape[axis]
    idx_sort = np.argsort(data, axis=axis)
    index_q = np.around((N - 1) * q / 100.0)
    result = np.take_along_axis(data, np.expand_dims(np.array(idx_sort), axis=axis), axis=axis)
    return result.take(int(index_q), axis=axis)

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 50
axis = 0
qth_quantile = compute_qth_quantile(data, q, axis)
print("Qth Quantile:", qth_quantile)
