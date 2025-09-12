import numpy as np
from scipy.ndimage import gaussian_filter

# Create a sample multidimensional array (e.g., a 2D array)
sample_array = np.random.rand(10, 10)

# Apply a Gaussian filter
# sigma represents the standard deviation for the Gaussian kernel, adjust as required
filtered_array = gaussian_filter(sample_array, sigma=1)
