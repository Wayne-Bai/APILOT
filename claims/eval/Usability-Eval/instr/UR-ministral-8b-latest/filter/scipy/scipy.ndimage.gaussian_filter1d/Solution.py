import scipy
from scipy.ndimage import gaussian_filter

# Sample 1-D data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Apply 1-D Gaussian filter
filtered_data = gaussian_filter(data, sigma=2)

print(filtered_data)
