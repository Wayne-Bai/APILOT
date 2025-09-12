import numpy as np
from scipy.ndimage import gaussian_filter1d

# Sample data
data = np.random.rand(100)

# Parameters
sigma = 2.0  # Standard deviation for Gaussian kernel

# Applying the Gaussian filter
filtered_data = gaussian_filter1d(data, sigma=sigma)

print(filtered_data)
