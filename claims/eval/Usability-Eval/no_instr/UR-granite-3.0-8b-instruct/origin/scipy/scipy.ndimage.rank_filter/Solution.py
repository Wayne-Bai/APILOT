from scipy.ndimage import rank_filter

# Assuming 'image' is your multidimensional array
# Replace 'window_size' with the desired window size for the filter
filtered_image = rank_filter(image, size=window_size, footprint=None, origin=0)
