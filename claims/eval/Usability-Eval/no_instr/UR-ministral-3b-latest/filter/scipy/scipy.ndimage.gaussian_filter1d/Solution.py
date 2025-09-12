
import scipy

def gaussian_filter(x, sigma=1):
    """
    Apply a 1-D Gaussian filter to an array `x`.

    Parameters:
        x (ndarray): Input array.
        sigma (float): Standard deviation of the Gaussian.

    Returns:
        ndarray: Filtered array.
    """

    # Compute the 1-D Gaussian kernel
    kernel = scipy.signal.gaussian(sigma, std=sigma)

    # Ensure that the kernel sum is 1
    kernel /= kernel.sum()

    # Apply the filter using convolution
    return scipy.signal.convolve(x, kernel, mode='same')

# Example usage
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
filtered_x = gaussian_filter(x, sigma=1)
print(filtered_x)
