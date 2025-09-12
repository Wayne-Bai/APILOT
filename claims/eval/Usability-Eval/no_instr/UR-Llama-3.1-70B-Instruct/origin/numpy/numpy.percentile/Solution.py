import numpy as np

def calculate_percentile(data, q, axis=None):
    """
    Compute the q-th percentile of the data along the specified axis.

    Args:
    data (numpy.ndarray): Input data.
    q (float or sequence of floats): Percentile to compute.
    axis (int or tuple, optional): Axis or axes along which to calculate the percentile. 
                                   The default is to compute the percentile(s) along a flattened version of the array.

    Returns:
    float or numpy.ndarray: The q-th percentile(s) of the array elements.
    """
    return np.percentile(data, q, axis=axis)

# Example usage
if __name__ == "__main__":
    # Create a sample numpy array
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Calculate the 50th percentile (median) along axis 0
    percentile = calculate_percentile(data, 50, axis=0)
    print(f"50th percentile along axis 0: {percentile}")

    # Calculate the 25th and 75th percentiles along axis 1
    percentiles = calculate_percentile(data, [25, 75], axis=1)
    print(f"25th and 75th percentiles along axis 1: {percentiles}")
