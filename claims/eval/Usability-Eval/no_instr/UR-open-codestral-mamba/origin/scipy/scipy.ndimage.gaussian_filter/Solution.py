import scipy.ndimage as ndimage

# Assume we have a 2D image represented by a numpy array `image`

# We want to perform a Gaussian filter with a standard deviation of 1 pixel
# over the y and x dimensions.

filtered_image = ndimage.gaussian_filter(image, sigma=(1, 1))

print(filtered_image)
