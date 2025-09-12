import numpy as np

def compute_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.

    Parameters:
    data : array_like
        Input array or object that can be converted to an array.
    q : float in range of [0,100] (or sequence of floats)
        Percentile to compute, which must be between 0 and 100 inclusive.
    axis : int, optional
        Axis along which the percentiles are computed. The default is to compute
        the percentile(s) along a flattened version of the array.

    Returns:
    percentile : scalar or ndarray
        If `q` is a single percentile, return a scalar. If multiple percentiles
        are given, first axis of the result corresponds to the percentiles.
    """
    # Ensure q is a list or array
    if not isinstance(q, (list, np.ndarray)):
        q = [q]
    
    # Flatten the array if axis is None
    if axis is None:
        data = data.flatten()
        axis = 0
    
    # Sort the data along the specified axis
    sorted_data = np.sort(data, axis=axis)
    
    # Calculate the indices for the percentiles
    n = sorted_data.shape[axis]
    indices = [(q_val / 100) * (n - 1) for q_val in q]
    
    # Compute the percentiles
    percentiles = []
    for idx in indices:
        lower_idx = int(np.floor(idx))
        upper_idx = int(np.ceil(idx))
        if lower_idx == upper_idx:
            percentile = np.take(sorted_data, lower_idx, axis=axis)
        else:
            lower_val = np.take(sorted_data, lower_idx, axis=axis)
            upper_val = np.take(sorted_data, upper_idx, axis=axis)
            percentile = lower_val + (idx - lower_idx) * (upper_val - lower_val)
        percentiles.append(percentile)
    
    # Return the result as a scalar or ndarray
    if len(q) == 1:
        return percentiles[0]
    else:
        return np.array(percentiles)

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 50
axis = 0
result = compute_percentile(data, q, axis)
print(result)
