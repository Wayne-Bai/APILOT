import numpy as np

def weighted_average(arr, weights, axis=None):
    """
    Returns the weighted average of an array over the specified axis.
    
    Parameters:
    arr (ndarray): Input array.
    weights (array-like): An array of weights associated with the values in arr.
    axis (int, optional): Axis along which to compute the weighted average. 
                          Default is to compute the weighted average of the flattened array.
    
    Returns:
    ndarray: Weighted average along the specified axis.
    """
    arr = np.array(arr)
    weights = np.array(weights)

    if axis is not None:
        # Expand dimensions of weights to match the shape of arr for broadcasting
        weights = np.expand_dims(weights, axis=(axis if axis >= 0 else axis + arr.ndim))
        
    weighted_sum = np.sum(arr * weights, axis=axis)
    sum_of_weights = np.sum(weights, axis=axis)
    
    return weighted_sum / sum_of_weights

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.1, 0.3, 0.6])

result = weighted_average(data, weights, axis=1)
print("Weighted average:", result)
