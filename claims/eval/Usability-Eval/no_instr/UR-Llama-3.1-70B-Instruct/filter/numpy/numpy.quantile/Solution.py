import numpy as np

def compute_quantile(data, q, axis):
    """
    Compute the q-th quantile of the data along the specified axis.

    Args:
        data (numpy.ndarray): Input data.
        q (float): Quantile to compute. Must be between 0 and 1.
        axis (int): Axis along which to compute the quantile.

    Returns:
        float or numpy.ndarray: The q-th quantile of the data.
    """

    # Check if axis is within bounds
    if axis < 0 or axis >= len(data.shape):
        raise ValueError("Axis out of bounds")

    # Check if quantile is within bounds
    if q < 0 or q > 1:
        raise ValueError("Quantile must be between 0 and 1")

    # Use numpy's sort and indexing to compute the quantile
    sorted_data = np.sort(data, axis=axis)

    # Calculate the index of the quantile
    index = q * (sorted_data.shape[axis] - 1)

    # If the index is an integer, return the value at that index
    if index == int(index):
        return np.take(sorted_data, int(index), axis=axis)

    # If the index is not an integer, interpolate between the two nearest values
    else:
        lower_index = int(np.floor(index))
        upper_index = int(np.ceil(index))
        lower_value = np.take(sorted_data, lower_index, axis=axis)
        upper_value = np.take(sorted_data, upper_index, axis=axis)
        return lower_value + (upper_value - lower_value) * (index - lower_index)


# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 0.5  # Compute the 50th percentile (median)
axis = 1  # Compute along the columns

print(compute_quantile(data, q, axis))
