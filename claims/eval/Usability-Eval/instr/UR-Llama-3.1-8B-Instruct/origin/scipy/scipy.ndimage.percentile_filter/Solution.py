import numpy as np
from scipy import stats
from scipy.interpolate import interp1d
import numpy.ma as ma

def multidimensional_percentile_filter(data, percentile):
    """
    Calculate a multidimensional percentile filter.

    Parameters:
    data (numpy array): Input data
    percentile (float): Percentile value to filter

    Returns:
    filtered_data (numpy array): Filtered data
    """
    # Get the shape of the input data
    rows, cols = data.shape

    # Reshape the data into a 1D array
    data_1d = data.flatten()

    # Calculate the percentile value
    percentile_value = np.percentile(data_1d, percentile)

    # Use scipy.stats.scoreatpercentile to find the percentage above/below the given
    percentage_above = np.sum(data_1d > percentile_value)
    percentage_below = np.sum(data_1d < percentile_value)

    filtered_data = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            # Use maximum/minimum based on the percentile
            if percentage_above > percentage_below:
                filtered_data[i, j] = np.percentile(data_1d[data_1d > percentile_value], percentile)
            else:
                filtered_data[i, j] = np.percentile(data_1d[data_1d < percentile_value], percentile)

    return filtered_data

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
percentile = 50
filtered_data = multidimensional_percentile_filter(data, percentile)
print(filtered_data)
