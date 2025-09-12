import numpy as np
from scipy.ndimage import filters

# Create a sample 3D image with noise
img = np.random.rand(10, 10, 10)

# Define the size of the minimum filter
size = (3, 3, 3)

# Apply the minimum filter to the image
min_filtered_img = filters.minimum_filter(img, size=size, mode='reflect')
