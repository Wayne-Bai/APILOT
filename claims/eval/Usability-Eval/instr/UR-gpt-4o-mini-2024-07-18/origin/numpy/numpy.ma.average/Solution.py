import numpy as np

def weighted_average(arr, weights, axis=None):
    """
    Compute the weighted average of an array over a specified axis.

    Parameters:
    arr (numpy.ndarray): Input array.
    weights (numpy.ndarray): Weights for each element in the array.
    axis (int, optional): Axis along which to compute the weighted average. 
                          If None, compute the average over the entire array.

    Returns:
    numpy.ndarray: Weighted average of the array along the specified axis.
    """
    # Normalize weights
    weights_normalized = weights / np.sum(weights, axis=axis, keepdims=True)
    
    # Calculate weighted average
    weighted_avg = np.sum(arr * weights_normalized, axis=axis)
    
    return weighted_avg
