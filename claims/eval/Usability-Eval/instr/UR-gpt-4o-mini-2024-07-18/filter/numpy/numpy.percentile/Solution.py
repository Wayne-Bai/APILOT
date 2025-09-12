import numpy as np

def compute_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.
    
    Parameters:
    data (array_like): Input data.
    q (float or array_like): The percentile(s) to compute, which must be between 0 and 100.
    axis (int, optional): Axis along which the percentiles are computed. 
                          By default, the flattened input array is used.
    
    Returns:
    ndarray: The q-th percentile(s) of the input data.
    """
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
q = 50  # 50th percentile (median)
percentile_value = compute_percentile(data, q, axis=0)
print("50th percentile along axis 0:", percentile_value)
