import numpy as np
from scipy.ndimage import median_filter

# Example data
data = np.random.rand(10, 10)  # Generating a random 10x10 array

# Apply median filter
filtered_data = median_filter(data, size=3)  # Using a 3x3 neighborhood
print(filtered_data)
