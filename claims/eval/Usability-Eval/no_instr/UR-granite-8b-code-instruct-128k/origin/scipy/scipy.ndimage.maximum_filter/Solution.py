import scipy.ndimage as ndimage

# Create a 3D array of random values
data = np.random.rand(10, 10, 10)

# Apply the maximum filter to the data
filtered_data = ndimage.filters.maximum_filter(data)
