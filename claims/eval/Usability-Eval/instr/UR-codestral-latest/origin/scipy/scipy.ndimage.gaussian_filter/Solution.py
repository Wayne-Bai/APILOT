import scipy.ndimage
import numpy as np

# Assuming you have a 2D array data
data = np.random.random((50, 50))

# Apply Gaussian filter with sigma=3
filtered_data = scipy.ndimage.gaussian_filter(data, sigma=3)
