import numpy as np

# Define a function to compute the q-th quantile of the data along the specified axis
def compute_quantile(data, q, axis):
    """
    Compute the q-th quantile of the data along the specified axis.

    Parameters:
    data (array): Input data
    q (float): Quantile value between 0 and 1
    axis (int): Axis along which to compute the quantile

    Returns:
    array: The computed quantile
    """
    return np.percentile(data, q * 100, axis=axis)

# Example usage:
# Create a sample array with two dimensions
data = np.array([[1, 3, 5], [2, 4, 6]])

# Compute the 0.5 quantile (median) along the 0 axis (default is to compute along all axes)
quantile = compute_quantile(data, 0.5, 0)
print("Median along the 0 axis:", quantile)

# Compute the 0.5 quantile along the 1 axis (compute along the second dimension)
quantile = compute_quantile(data, 0.5, 1)
print("Median along the 1 axis:", quantile)
