import numpy as np

def compute_percentile(data, q):
    """
    Computes the q-th percentile of the data along the specified axis.

    Parameters:
    data (numpy.ndarray): The input data array.
    q (float): The percentile value.

    Returns:
    numpy.ndarray: The q-th percentile(s) of the data elements.
    """
    if not 0 <= q <= 100:
        raise ValueError("q must be between 0 and 100")

    percentile = np.percentile(data, q)
    return percentile
