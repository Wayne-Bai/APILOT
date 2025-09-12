import numpy as np

def weighted_average(arr, weights, axis=None):
    """
    Calculate the weighted average of an array.

    Parameters:
    arr (numpy array): Input array.
    weights (numpy array): Weights for calculating weighted average.
    axis (int, optional): Axis over which the weighted average is calculated. Defaults to None.

    Returns:
    numpy array: Weighted average of the input array.
    """
    # Calculate the weighted sum
    weighted_sum = np.sum(arr * weights, axis=axis)
    
    # Calculate the sum of weights
    sum_weights = np.sum(weights, axis=axis)
    
    # Calculate the weighted average
    weighted_avg = weighted_sum / sum_weights
    
    return weighted_avg

# Example usage:
if __name__ == "__main__":
    # Create a numpy array
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # Create weights
    weights = np.array([[0.2, 0.3, 0.5], [0.1, 0.2, 0.7]])

    # Calculate weighted average over axis 0
    weighted_avg_axis_0 = weighted_average(arr, weights, axis=0)
    print("Weighted Average (Axis 0):")
    print(weighted_avg_axis_0)

    # Calculate weighted average over axis 1
    weighted_avg_axis_1 = weighted_average(arr, weights, axis=1)
    print("\nWeighted Average (Axis 1):")
    print(weighted_avg_axis_1)
