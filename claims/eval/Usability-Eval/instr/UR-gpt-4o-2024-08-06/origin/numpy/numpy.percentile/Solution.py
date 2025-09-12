import numpy as np

def compute_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.

    Parameters:
    data (array-like): Input array or object that can be converted to an array.
    q (float or array-like): Percentile or sequence of percentiles to compute, which must be between 0 and 100 inclusive.
    axis (int, optional): Axis along which the percentiles are computed. Default is to compute the percentile over the flattened array.

    Returns:
    percentile (ndarray): The q-th percentile(s) of the array elements.
    """
    # Validate the percentile value(s)
    if np.any((np.asarray(q) < 0) | (np.asarray(q) > 100)):
        raise ValueError("Percentile must be in the range [0, 100]")
    
    # Compute the percentile and return
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 50  # 50th percentile, also known as the median
percentile = compute_percentile(data, q, axis=0)
print(f"{q}-th percentile along axis 0:\n", percentile)
