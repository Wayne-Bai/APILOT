import scipy.ndimage as ndimage

def gaussian_filter(image, sigma):
    return ndimage.gaussian_filter(image, sigma)

image = ...
sigma = ...
filtered_image = gaussian_filter(image, sigma)