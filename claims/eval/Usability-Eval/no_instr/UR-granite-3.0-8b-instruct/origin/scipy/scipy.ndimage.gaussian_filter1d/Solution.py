from scipy.ndimage import gaussian_filter1d

# Assuming 'data' is your 1D array
filtered_data = gaussian_filter1d(data, sigma=1)
