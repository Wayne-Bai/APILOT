import numpy as np
from scipy.ndimage import gaussian_filter

# Assuming 'image' is your multidimensional input data
# Replace 'sigma' with the desired standard deviation for the Gaussian filter
filtered_image = gaussian_filter(image, sigma=sigma)
