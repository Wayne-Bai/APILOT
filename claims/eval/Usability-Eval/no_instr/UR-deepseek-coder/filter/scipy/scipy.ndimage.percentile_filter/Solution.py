import numpy as np
from scipy.ndimage import percentile_filter

# Example usage:
data = np.random.rand(10, 10)  # Example 2D array
percentile = 50  # Example percentile (50th percentile is the median)
size = 3  # Size of the window for the filter

# Apply the percentile filter
filtered_data = percentile_filter(data, percentile, size=size)

print(filtered_data)
