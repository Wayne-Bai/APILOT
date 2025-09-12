from scipy.ndimage import convolve
import numpy as np

def gaussian_kernel(size, sigma):
    """
    Generates a multidimensional Gaussian kernel.

    Args:
        size (int): Size of the kernel.
        sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
        numpy.ndarray: The Gaussian kernel.
    """
    # Create a grid of coordinates
    x = np.arange(-(size // 2), size // 2 + 1)
    x, y = np.meshgrid(x, x)

    # Calculate the Gaussian distribution
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)

    return kernel

def multidimensional_gaussian_filter(data, size, sigma):
    """
    Applies a multidimensional Gaussian filter to the data.

    Args:
        data (numpy.ndarray): Input data.
        size (int): Size of the kernel.
        sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
        numpy.ndarray: The filtered data.
    """
    # Generate the Gaussian kernel
    kernel = gaussian_kernel(size, sigma)

    # Apply the filter to each dimension
    filtered_data = data
    for axis in range(data.ndim):
        # Use the convolve function to apply the filter
        filtered_data = convolve(filtered_data, kernel, axis=axis, mode='constant')

    return filtered_data

# Example usage
if __name__ == "__main__":
    # Create some example data
    data = np.random.rand(256, 256)

    # Apply the filter
    filtered_data = multidimensional_gaussian_filter(data, size=5, sigma=1)

    # Print the result
    print("Filtered Data:\n", filtered_data)
