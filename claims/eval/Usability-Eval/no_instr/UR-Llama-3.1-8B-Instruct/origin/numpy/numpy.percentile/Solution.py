import numpy as np

def compute_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.

    Parameters:
    data (numpy array): Input data.
    q (float or array-like): Percentage to compute the percentile from (0 to 100).
    axis (int or None): Axis along which the percentile computation is performed.

    Returns:
    p (float or numpy array): Percentile(s) of the data.
    """
    try:
        p = np.percentile(data, q, axis)
        return p
    except ValueError as e:
        print(f"Invalid input: {e}")

# Example usage
data = np.array([1, 2, 3, 4, 5])
q = 50
print(compute_percentile(data, q))

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
q = [25, 50, 75]
print(compute_percentile(data, q, axis=0))

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 50
print(compute_percentile(data, q, axis=1))
