import numpy as np

def compute_quantile(data, q, axis):
    """
    Compute the q-th quantile of the data along the specified axis.

    Parameters:
    data (numpy.ndarray): Input data.
    q (float): Quantile to compute (0 <= q <= 1).
    axis (int): Axis along which to compute the quantile.

    Returns:
    numpy.ndarray: Quantile of the data along the specified axis.
    """
    return np.quantile(data, q, axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 0.5
axis = 0

quantile_value = compute_quantile(data, q, axis)
print("Quantile along axis {}: {}".format(axis, quantile_value))
