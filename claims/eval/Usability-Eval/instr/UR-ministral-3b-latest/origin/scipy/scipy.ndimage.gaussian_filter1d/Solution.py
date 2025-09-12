import scipy.ndimage as ndimage

# Define the Gaussian filter
sigma = 1.0
gaussian_filter = ndimage.gaussian_filter1d

# Apply the Gaussian filter
result = gaussian_filter(x, sigma)
