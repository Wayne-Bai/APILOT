import scipy.ndimage

def multidimensional_median_filter(image, size):
    """
    Applies a multidimensional median filter on a given image.

    Parameters:
        image (ndarray): Input image (2D, 3D, or higher dimensional).
        size (tuple): Median filter size as a tuple of integers. The size of the
                      neighborhood around the pixel to which the filter is
                      applied.

    Returns:
        ndarray: Processed image with median filter applied.
    """
    # Use scipy's ndimage's median_filter for 2D images
    if len(image.shape) == 2:
        return scipy.ndimage.median_filter(image, size)
    else:
        # In case of higher-dimensional inputs, use np.median along the last axis
        return np.median(image, axis=-1)
