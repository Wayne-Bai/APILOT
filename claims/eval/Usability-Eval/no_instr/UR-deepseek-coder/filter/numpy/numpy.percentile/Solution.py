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
    return np.percentile(data, q, axis=axis)
