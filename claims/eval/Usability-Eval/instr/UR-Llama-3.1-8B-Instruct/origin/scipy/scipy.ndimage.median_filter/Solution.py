from scipy import ndimage
import numpy as np

# Define a 2D array for demonstration
# Replace this with your actual data
data = np.random.rand(10, 10)

# Apply a 3x3 median filter
filtered_data = ndimage.median_filter(data, size=3)

print(filtered_data)
