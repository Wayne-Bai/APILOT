import numpy as np
from scipy.ndimage import generic_filter

def multidimensional_percentile_filter(data, percentiles, size):
    filtered_data = generic_filter(data, percentiles, footprint=np.ones(size)*(size[0]*size[1]-1), mode='reflect', cval=None)
    return filtered_data

# Example usage:
data = np.random.rand(5, 5)
percentiles = np.percentile(data, [25, 75], axis=(1, 2))  # Calculate 25th and 75th percentile along each point
size = (5, 5)

filtered_data = multidimensional_percentile_filter(data, percentiles, size)
print(filtered_data)
