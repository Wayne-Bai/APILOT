from scipy.ndimage import generic_filter

def percentile_filter(data, weights, dtype):
    """
    Apply a percentile filter to the input data using generic_filter

    Parameters:
        data (ndarray): input data for the filter
        weights (list): weights for each percentile value
        dtype (str): data type of the output filter

    Returns:
        ndarray: filtered data
    """
    return generic_filter(data, np.percentile, size=weights, mode='nearest')

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
weights = (80, 50)  # percentile weights
output = percentile_filter(data, weights, dtype=np.float32)
print(output)
