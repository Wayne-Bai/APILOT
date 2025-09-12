import numpy as np
from scipy.ndimage import gaussian_filter

# Create a 3D array for this example
data = np.random.rand(10, 10, 10)

# Apply Gaussian filter with standard deviation (sigma) of 1
filtered_data = gaussian_filter(data, sigma=1)
