from scipy.ndimage import uniform_filter

# Assuming 'data' is your multidimensional array
filtered_data = uniform_filter(data, size=3)
