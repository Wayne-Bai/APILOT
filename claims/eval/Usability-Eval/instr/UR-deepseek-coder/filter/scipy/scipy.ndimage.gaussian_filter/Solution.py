import numpy as np
from scipy.ndimage import gaussian_filter

# Example usage:
# Create a sample 2D array
data = np.random.rand(100, 100)

# Apply a Gaussian filter with a sigma of 2
filtered_data = gaussian_filter(data, sigma=2)

print(filtered_data)
