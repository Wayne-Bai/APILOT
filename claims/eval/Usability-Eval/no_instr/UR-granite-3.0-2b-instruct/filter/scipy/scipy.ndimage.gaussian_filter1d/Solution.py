import numpy as np
from scipy.ndimage import gaussian_filter1d

# Sample 1-D data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Apply 1-D Gaussian filter
filtered_data = gaussian_filter1d(data, sigma=2)

print(filtered_data)
