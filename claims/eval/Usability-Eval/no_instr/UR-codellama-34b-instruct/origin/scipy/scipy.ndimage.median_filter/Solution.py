import numpy as np
from scipy.ndimage import median_filter

# Generate some sample data
data = np.random.rand(10, 10)

# Calculate the median filter for each pixel
median_filtered_data = median_filter(data, size=(3, 3))

print(median_filtered_data)
