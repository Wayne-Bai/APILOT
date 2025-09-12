import numpy as np
from scipy.ndimage import gaussian_filter

# Create a sample multidimensional numpy array
data = np.random.rand(5, 5)

# Apply a Gaussian filter with a specified sigma
sigma = 1.0
filtered_data = gaussian_filter(data, sigma=sigma)

print("Original Data:")
print(data)
print("\nFiltered Data:")
print(filtered_data)
