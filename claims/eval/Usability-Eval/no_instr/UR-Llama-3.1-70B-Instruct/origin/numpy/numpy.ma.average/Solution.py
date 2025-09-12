import numpy as np

def weighted_average(arr, weights, axis=0):
    """
    Return the weighted average of array over the given axis.

    Parameters:
    arr (numpy.ndarray): Input array.
    weights (numpy.ndarray): Weights for the average.
    axis (int, optional): Axis over which to calculate the weighted average. Default is 0.

    Returns:
    numpy.ndarray: Weighted average of the array over the given axis.
    """
    # Ensure arr and weights are numpy arrays
    arr = np.asarray(arr)
    weights = np.asarray(weights)

    # Check if arr and weights have the same shape
    if arr.shape!= weights.shape:
        raise ValueError("Array and weights must have the same shape")

    # Calculate the weighted sum along the given axis
    weighted_sum = np.sum(arr * weights, axis=axis)

    # Calculate the sum of weights along the given axis
    sum_weights = np.sum(weights, axis=axis)

    # Calculate the weighted average
    weighted_avg = weighted_sum / sum_weights

    return weighted_avg

# Example usage
arr = np.arange(12).reshape(3, 4)
weights = np.array([1, 2, 3])[:, None]

print("Array:")
print(arr)
print("Weights:")
print(weights)

weighted_avg = weighted_average(arr, weights, axis=1)
print("Weighted average:")
print(weighted_avg)
