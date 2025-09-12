from scipy.ndimage import gaussian_filter1d

# Assuming 'data' is your 1D array
data = ...

# Apply 1D Gaussian filter
filtered_data = gaussian_filter1d(data, sigma=1.0)
