from scipy.ndimage import gaussian_filter

def multidimensional_gaussian_filter(image, sigma):
    """
    This function applies a multidimensional Gaussian filter to the input image.

    Parameters:
    image (numpy.ndarray): The input multidimensional image.
    sigma (float or numpy.ndarray): The standard deviation for the Gaussian filter. If a float, it will be applied uniformly to all dimensions. If a numpy array, it should have the same shape as the input image and will be applied independently to each dimension.

    Returns:
    numpy.ndarray: The filtered image.
    """
    if isinstance(sigma, (int, float)):
        sigma = np.ones_like(image) * sigma

    # Ensure the input image is a numpy array
    image = np.array(image)

    # Apply the Gaussian filter
    filtered_image = gaussian_filter(image, sigma)

    return filtered_image
