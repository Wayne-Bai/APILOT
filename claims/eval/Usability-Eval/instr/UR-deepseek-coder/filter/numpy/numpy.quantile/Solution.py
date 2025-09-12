import numpy as np

def compute_quantile(data, q, axis=None):
    sorted_data = np.sort(data, axis=axis)
    if axis is None:
        n = sorted_data.size
    else:
        n = sorted_data.shape[axis]
    
    if q == 0:
        return sorted_data.min(axis=axis)
    elif q == 1:
        return sorted_data.max(axis=axis)
    
    index = q * (n - 1)
    lower_index = int(index)
    upper_index = lower_index + 1
    fraction = index - lower_index
    
    if axis is None:
        lower_value = sorted_data[lower_index]
        upper_value = sorted_data[upper_index]
    else:
        lower_value = np.take(sorted_data, lower_index, axis=axis)
        upper_value = np.take(sorted_data, upper_index, axis=axis)
    
    return lower_value + fraction * (upper_value - lower_value)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 0.5  # Median
quantile_value = compute_quantile(data, q, axis=0)
print(quantile_value)
