import scipy.ndimage as ndimage

# Assuming 'image' is a multidimensional array (e.g., a 2D image or 3D data).
# The size of the filtering window can be specified with the 'size' parameter.
def apply_uniform_filter(image, size):
    filtered_image = ndimage.uniform_filter(image, size=size)
    return filtered_image
