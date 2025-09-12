import numpy as np
import scipy.ndimage

# Example multidimensional array
data = np.array([
    [5, 3, 8, 4],
    [2, 1, 9, 6],
    [7, 4, 3, 8],
    [6, 5, 2, 1]
])

# Define the size of the filter
filter_size = 2

# Apply a multidimensional minimum filter
min_filtered_data = scipy.ndimage.minimum_filter(data, size=filter_size)

print("Original Data:\n", data)
print("Minimum Filtered Data:\n", min_filtered_data)
