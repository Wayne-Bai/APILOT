import numpy as np
from scipy.ndimage import median_filter

# Create a 2D array to filter
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply the median filter with a kernel size of 3x3
filtered_data = median_filter(data, size=(3, 3))

# Print the filtered data
print(filtered_data)
