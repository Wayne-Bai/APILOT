import numpy as np
from scipy.ndimage import gaussian_filter1d

# Example data: 1-D signal
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Apply a 1-D Gaussian filter
# sigma determines the standard deviation of the Gaussian function
sigma = 1.0
filtered_data = gaussian_filter1d(data, sigma)

print("Original Data: ", data)
print("Filtered Data: ", filtered_data)
