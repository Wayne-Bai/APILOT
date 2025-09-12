import numpy as np

def compute_quantile(data, q, axis=None):
    """
    Compute the q-th quantile of the data along the specified axis.

    Parameters:
    data (array_like): Input data.
    q (float): Quantile to compute, which must be between 0 and 1 inclusive.
    axis (int, optional): Axis along which the quantiles are computed. By default, the quantile is computed for the flattened array.

    Returns:
    ndarray: The q-th quantile of the array elements along the specified axis.
    """
    if not (0 <= q <= 1):
        raise ValueError("q must be between 0 and 1 inclusive.")
    
    return np.quantile(data, q, axis=axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6]])
q = 0.5
quantile_result = compute_quantile(data, q, axis=0)
print(quantile_result)
