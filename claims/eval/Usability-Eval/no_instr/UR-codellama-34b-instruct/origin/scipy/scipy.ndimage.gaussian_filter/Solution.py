import numpy as np
from scipy.ndimage import gaussian_filter

# Load the image data
img = np.load('image.npy')

# Define the parameters for the Gaussian filter
sigma = 1.0 # standard deviation in pixels
order = 3 # order of the filter (3 is a good default value)

# Apply the Gaussian filter to the image
filtered_img = gaussian_filter(img, sigma=sigma, order=order)
