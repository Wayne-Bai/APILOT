from scipy import ndimage

def multidimensional_minimum_filter(image, block_size):
    """
    This function applies a multidimensional minimum filter to the input image.

    Parameters:
    image (numpy.ndarray): The input multidimensional image.
    block_size (int): The size of the filter block.

    Returns:
    numpy.ndarray: The filtered image.
    """
    return ndimage.minimum_filter(image, size=block_size)
