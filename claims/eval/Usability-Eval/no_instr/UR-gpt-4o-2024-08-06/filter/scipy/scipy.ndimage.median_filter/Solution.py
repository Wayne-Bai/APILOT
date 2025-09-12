import numpy as np
from scipy.ndimage import median_filter

# Example: Apply median filter to a 2D array
data = np.array([[10, 20, 30, 40],
                 [40, 180, 60, 90],
                 [60, 70, 80, 90],
                 [90, 100, 110, 120]])

# Define the size of the filter, e.g. a 3x3 median filter
filter_size = 3

# Apply the median filter
filtered_data = median_filter(data, size=filter_size)

print("Original Data:")
print(data)
print("\nFiltered Data:")
print(filtered_data)
