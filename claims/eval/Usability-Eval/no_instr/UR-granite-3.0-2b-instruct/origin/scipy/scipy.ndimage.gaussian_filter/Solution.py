from scipy.ndimage import gaussian_filter

def multidimensional_gaussian_filter(data, sigma):
    """
    Applies a multidimensional Gaussian filter to the input data.

    Parameters:
    data (numpy.ndarray): The input multidimensional data.
    sigma (float or numpy.ndarray): The standard deviation for the Gaussian filter.
                                   If a single value is provided, it will be applied to all dimensions.
                                   If a numpy array is provided, it should have the same number of elements as the number of dimensions.

    Returns:
    numpy.ndarray: The filtered data.
    """
    if isinstance(sigma, (int, float)):
        sigma = np.full_like(data, sigma)

    return gaussian_filter(data, sigma)
