import numpy as np
from scipy.ndimage import maximum_filter

# Sample 2D array
data = np.array([
    [1, 2, 3, 2, 1],
    [4, 5, 6, 5, 4],
    [7, 8, 9, 8, 7],
    [4, 5, 6, 5, 4],
    [1, 2, 3, 2, 1]
])

# Define the size of the filter
filter_size = 3

# Apply the maximum filter to the data
max_filtered_data = maximum_filter(data, size=filter_size)

print("Original Data:")
print(data)
print("\nMax Filtered Data:")
print(max_filtered_data)
