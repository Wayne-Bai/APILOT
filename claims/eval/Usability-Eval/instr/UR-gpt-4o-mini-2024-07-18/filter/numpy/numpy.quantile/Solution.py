import numpy as np

def compute_quantile(data, q, axis=None):
    """
    Compute the q-th quantile of the data along the specified axis.

    Parameters:
    data (array_like): Input data.
    q (float): Quantile to compute, which must be between 0 and 1.
    axis (int, optional): Axis along which the quantile is computed. 
                          By default, the quantile is computed over the entire array.

    Returns:
    float or ndarray: The q-th quantile of the array elements.
    """
    if not (0 <= q <= 1):
        raise ValueError("Quantile q must be in the range [0, 1]")

    return np.percentile(data, q * 100, axis=axis)
