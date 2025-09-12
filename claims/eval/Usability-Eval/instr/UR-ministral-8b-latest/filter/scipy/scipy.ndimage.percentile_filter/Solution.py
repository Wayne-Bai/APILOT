import numpy as np
import scipy

# Define a function to apply a multidimensional percentile filter
def multidimensional_percentile_filter(data, p=None):
    # Convert to numpy array
    data = np.array(data)

    # Calculate the p-th percentile
    p_values = np.percentile(data, p)

    # Replace values below the percentile with NaN
    data_mask = data < p_values
    data[data_mask] = np.nan

    return data

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
percentile_filtered_data = multidimensional_percentile_filter(data, 50)
print(percentile_filtered_data)
