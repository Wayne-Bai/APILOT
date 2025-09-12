import numpy as np

def percentile(arr, q, axis=None):
    """
    Compute the q-th percentile of the array elements along the specified axis.

    Parameters:
    arr (numpy.ndarray): Input array.
    q (float): Percentile to compute. It should be between 0 and 100.
    axis (int, optional): Axis along which to compute the percentile. If None, compute over the flattened array.

    Returns:
    numpy.ndarray: The q-th percentile(s) of the array elements.
    """
    if not 0 <= q <= 100:
        raise ValueError("Percentile must be between 0 and 100.")

    if axis is None:
        arr = arr.flatten()

    return np.percentile(arr, q, axis=axis)
