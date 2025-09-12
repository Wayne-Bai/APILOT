import numpy as np

def compute_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.

    Parameters:
    - data: array-like, the input data.
    - q: float or array-like, the percentile(s) to compute (must be between 0 and 100).
    - axis: int, optional, the axis along which to compute the percentile. If None, compute over the flattened array.

    Returns:
    - percentile values: scalar or ndarray, the q-th percentile(s) of the input data.
    """
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
percentile_50 = compute_percentile(data, 50)  # Computation along a flattened array
percentile_axis_0 = compute_percentile(data, 50, axis=0)  # Computation along the first axis
percentile_axis_1 = compute_percentile(data, 50, axis=1)  # Computation along the second axis

print("50th percentile of flattened array:", percentile_50)
print("50th percentile along axis 0:", percentile_axis_0)
print("50th percentile along axis 1:", percentile_axis_1)
