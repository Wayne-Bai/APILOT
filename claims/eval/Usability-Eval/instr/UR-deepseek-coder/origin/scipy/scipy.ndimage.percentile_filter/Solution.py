import numpy as np
from scipy.ndimage import percentile_filter

# Example usage
data = np.random.rand(100, 100)  # Example 2D array
percentile = 50  # Example percentile (median filter)
size = 3  # Example window size

# Apply the percentile filter
filtered_data = percentile_filter(data, percentile, size=size)

print(filtered_data)
