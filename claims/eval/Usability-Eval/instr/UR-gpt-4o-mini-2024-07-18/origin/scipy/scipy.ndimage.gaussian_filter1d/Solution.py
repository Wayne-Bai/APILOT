import numpy as np
from scipy.ndimage import gaussian_filter1d

def apply_gaussian_filter_1d(data, sigma):
    """
    Apply a 1-D Gaussian filter to the input data.

    Parameters:
    data (numpy.ndarray): The input 1-D array to be filtered.
    sigma (float): The standard deviation for the Gaussian kernel.

    Returns:
    numpy.ndarray: The filtered data.
    """
    return gaussian_filter1d(data, sigma)

# Example usage:
if __name__ == "__main__":
    # Sample data
    data = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
    sigma = 1.0
    
    filtered_data = apply_gaussian_filter_1d(data, sigma)
    print(filtered_data)
