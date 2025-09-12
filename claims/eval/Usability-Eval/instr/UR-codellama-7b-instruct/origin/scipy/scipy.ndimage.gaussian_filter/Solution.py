import numpy as np
from scipy import signal

def multidimensional_gaussian_filter(data, sigma, truncate=4.0):
    """Apply a multidimensional Gaussian filter to the input data.
    
    Args:
        data (ndarray): The input data to be filtered.
        sigma (float or tuple of floats): The standard deviation of the Gaussian 
            kernel in each dimension. If a single value is given, it is used for all dimensions.
        truncate (float, optional): The truncation mode for the Gaussian kernel. Defaults to 4.0.
    
    Returns:
        ndarray: The filtered data.
    """
    data_shape = np.shape(data)
    n_dimensions = len(data_shape)
    
    # create a list of standard deviations for each dimension
    if isinstance(sigma, float):
        stds = [sigma] * n_dimensions
    else:
        stds = sigma
    
    # create a list of Gaussian kernels for each dimension
    gaussians = []
    for i in range(n_dimensions):
        gaussians.append(signal.gaussian(data_shape[i], stds[i], truncate=truncate))
    
    # convolve the data with the Gaussian kernels in each dimension
    filtered_data = np.copy(data)
    for i in range(n_dimensions):
        filtered_data = signal.convolve(filtered_data, gaussians[i], mode='same')
    
    return filtered_data
