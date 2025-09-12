import numpy as np

def compute_quantile(data, q, axis=None):
    """
    Compute the q-th quantile of the data along the specified axis.
    
    Parameters:
    data (array_like): Input data.
    q (float): Quantile to compute, which must be between 0 and 1 inclusive.
    axis (int, optional): Axis along which the quantiles are computed. Default is to compute the quantile of the flattened array.

    Returns:
    quantile : ndarray
        If `axis` is None, a scalar is returned. Otherwise, an array with the quantiles.
    """
    return np.quantile(data, q, axis=axis)

# Example Usage
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 0.5  # Median
quantile = compute_quantile(data, q, axis=0)
print(quantile)
