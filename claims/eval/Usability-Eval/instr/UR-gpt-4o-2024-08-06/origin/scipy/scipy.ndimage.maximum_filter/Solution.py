import numpy as np
from scipy.ndimage import maximum_filter

# Example array representing a 3D data set
data = np.random.rand(4, 4, 4)

# Define the size of the filter window, e.g., 3x3x3
size = 3

# Calculate the maximum filter
filtered_data = maximum_filter(data, size)

print("Original Data:")
print(data)
print("\nMaximum Filtered Data:")
print(filtered_data)
