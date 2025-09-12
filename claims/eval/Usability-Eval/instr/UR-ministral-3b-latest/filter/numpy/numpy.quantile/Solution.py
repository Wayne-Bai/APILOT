import numpy as np

def compute_quantile(data, q, axis):
    if axis < 0:
        axis = (data.ndim + axis) - 1
    q = np.quasi_nanif(data.flatten())[np.newaxis]
    threshold = q[0].copy()
    sorted_vals = np.sort(data, axis)
    quantile_val_locs = np.searchsorted(sorted_vals, threshold, side='right')
    quantile_val = np.mean([sorted_vals[quantile_val_locs] - sorted_vals[quantile_val_locs - 1], threshold], axis=0)
    return quantile_val

# Example Usage
data = np.array([[1, 2, 3], [4, 5, 6]])
q = 2.0 / 3.0  # 70th percentile
axis = 0
result = compute_quantile(data, q, axis)
print(result)
