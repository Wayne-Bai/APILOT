import numpy as np
from scipy.ndimage import gaussian_filter

def apply_gaussian_filter_1d(data, sigma):
    """
    Apply a 1-D Gaussian filter to the given data.
    
    :param data: (array-like) The 1D array of data to be filtered.
    :param sigma: (float) The standard deviation for Gaussian kernel.
    :return: (numpy.ndarray) The smoothed data.
    """
    # Apply Gaussian filter
    smoothed_data = gaussian_filter(data, sigma=sigma, mode='reflect')
    return smoothed_data

# Example usage
if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    sigma = 1.5
    smoothed_data = apply_gaussian_filter_1d(data, sigma)
    print("Original Data:", data)
    print("Smoothed Data:", smoothed_data)
