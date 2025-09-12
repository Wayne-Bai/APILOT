import numpy as np
from scipy.ndimage import percentile_filter

# Example data: 3D array
data = np.random.rand(4, 4, 4)

# Define the percentile and size of the filter
percentile = 50  # Median filter
size = 3  # 3x3x3 window will be used

# Apply the percentile filter
filtered_data = percentile_filter(data, percentile, size=size)

print("Original Data:\n", data)
print("\nFiltered Data:\n", filtered_data)
