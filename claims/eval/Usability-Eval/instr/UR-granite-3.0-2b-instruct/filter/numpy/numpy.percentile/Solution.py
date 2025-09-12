import numpy as np

def compute_percentile(data, q):
    """
    Compute the q-th percentile of the data along the specified axis.

    Parameters:
    data (numpy.ndarray): The input data.
    q (float): The percentile value.

    Returns:
    numpy.ndarray: The q-th percentile(s) of the data.
    """
    return np.percentile(data, q, axis=0)
