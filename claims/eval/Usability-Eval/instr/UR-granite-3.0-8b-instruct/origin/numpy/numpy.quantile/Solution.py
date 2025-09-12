import numpy as np

def compute_quantile(data, q, axis=None):
    """
    Compute the q-th quantile of the data along the specified axis.

    Parameters:
    data (numpy.ndarray): Input data.
    q (float): Quantile value between 0 and 1.
    axis (int, optional): Axis along which the quantile is computed. Default is None.

    Returns:
    numpy.ndarray: Quantile values.
    """
    return np.percentile(data, q, axis=axis)
