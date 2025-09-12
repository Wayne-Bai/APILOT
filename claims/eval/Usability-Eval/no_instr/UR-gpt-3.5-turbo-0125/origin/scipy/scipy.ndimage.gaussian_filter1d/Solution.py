
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Generate random 1D data
data = np.random.rand(100)

# Apply 1-D Gaussian filter with sigma = 1
filtered_data = gaussian_filter1d(data, sigma=1)

print(filtered_data)
