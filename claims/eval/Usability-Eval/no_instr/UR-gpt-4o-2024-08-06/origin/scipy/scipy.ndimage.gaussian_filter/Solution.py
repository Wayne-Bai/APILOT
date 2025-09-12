import numpy as np
from scipy.ndimage import gaussian_filter

# Sample multidimensional data (e.g., a 3D array)
data = np.random.random((5, 5, 5))

# Apply a Gaussian filter with a specified standard deviation
sigma = 1.0  # Standard deviation for Gaussian kernel
filtered_data = gaussian_filter(data, sigma=sigma)

# Display the filtered data
print("Original Data:\n", data)
print("\nFiltered Data:\n", filtered_data)
