from scipy.ndimage import rank_filter

def multidimensional_rank_filter(array, rank):
    """
    This function applies a multidimensional rank filter to the input array.

    Parameters:
    array (numpy.ndarray): The input multidimensional array.
    rank (int): The rank to be used in the filter.

    Returns:
    numpy.ndarray: The filtered array.
    """
    return rank_filter(array, rank)
