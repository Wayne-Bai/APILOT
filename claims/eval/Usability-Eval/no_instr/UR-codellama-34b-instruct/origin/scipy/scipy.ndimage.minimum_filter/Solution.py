import numpy as np
from scipy.ndimage import filters

# Generate a random image
img = np.random.rand(10, 10)

# Define the size of the filter
size = (3, 3)

# Calculate the minimum filter
min_filter = filters.minimum_filter(img, size=size, mode='reflect')
