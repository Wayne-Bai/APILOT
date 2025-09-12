import numpy as np

def weighted_average(arr, weights, axis=None):
    """
    Calculate the weighted average of an array over a given axis.
    
    Parameters
    ----------
    arr : ndarray
        The input array to calculate the weighted average for.
    weights : ndarray
        The weights to apply to each element in the array.
    axis : int, optional
        The axis along which to calculate the weighted average. If not specified, the average will be calculated over the entire array.
    
    Returns
    -------
    ndarray
        The weighted average of the input array along the specified axis.
    """
    # Weighted sum of elements in arr and weights arrays
    sum_weighted = np.sum(arr * weights, axis=axis)
    
    # Normalize by dividing by the sum of weights
    return np.divide(sum_weighted, np.sum(weights, axis=axis), out=np.zeros_like(arr))
