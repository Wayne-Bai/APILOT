import numpy as np
from scipy.ndimage import gaussian_filter1d

# Example data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Apply 1-D Gaussian filter with a standard deviation of 1.5
filtered_data = gaussian_filter1d(data, sigma=1.5)

print(filtered_data)
