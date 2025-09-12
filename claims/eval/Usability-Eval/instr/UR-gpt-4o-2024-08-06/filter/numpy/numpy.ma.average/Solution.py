import numpy as np

def weighted_average(arr, weights, axis=None):
    """
    Calculate the weighted average of a numpy array over a given axis.

    Parameters:
    arr (ndarray): Input array.
    weights (ndarray): An array of weights, which can be either 1-D or of the same shape as `arr`.
                       The weights must be broadcastable to the shape of `arr`.
    axis (int, optional): The axis along which to compute the weighted average.
                          If None, the weighted average is computed over the flattened array.

    Returns:
    float or ndarray: The weighted average along the specified axis.
    """
    if axis is None:
        weighted_sum = np.sum(arr * weights)
        sum_of_weights = np.sum(weights)
    else:
        weighted_sum = np.sum(arr * weights, axis=axis)
        sum_of_weights = np.sum(weights, axis=axis)
    
    return weighted_sum / sum_of_weights

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([[0.1, 0.2, 0.7], [0.3, 0.3, 0.4]])
result = weighted_average(arr, weights, axis=1)
print(result)  # Output will be the weighted average along axis 1
