from scipy import ndimage

def multidimensional_rank_filter(image, radius, mode):
    """
    This function applies a multidimensional rank filter to the input image.

    Parameters:
    image (numpy.ndarray): The input multidimensional image.
    radius (int): The radius of the filter.
    mode (str): The mode of the filter. Can be 'nearest', 'wrap', or 'reflect'.

    Returns:
    numpy.ndarray: The filtered image.
    """
    # Apply the rank filter along each dimension
    filtered_image = ndimage.rank_filter(image, radius, mode=mode)

    return filtered_image
