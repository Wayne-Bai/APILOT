import numpy as np
from scipy import ndimage

def multidimensional_gaussian_filter(image, sigma):
    """
    Applies a multidimensional Gaussian filter to an image.

    Parameters:
    image (numpy array): The input image.
    sigma (float): The standard deviation of the Gaussian filter.

    Returns:
    filtered_image (numpy array): The filtered image.
    """
    # Define the size of the filter kernel based on 6*sigma
    kernel_size = int(6 * sigma) + 1
    if kernel_size % 2 == 0:
        kernel_size += 1  # Make kernel size odd

    # Create a 1D Gaussian filter kernel
    gaussian_kernel = ndimage.gaussian_filter1d(np.ones(kernel_size), sigma, axis=0, cval=0)

    # Reshape the kernel to 2D
    kernel_2d = np.outer(gaussian_kernel, gaussian_kernel)

    # Normalize the kernel to ensure it sums up to 1
    kernel_2d /= np.sum(kernel_2d)

    # Apply the 2D Gaussian filter to the image
    filtered_image = ndimage.convolve(image, kernel_2d, mode='nearest')

    return filtered_image

# Example usage
if __name__ == "__main__":
    # Create a sample 2D image
    image = np.random.rand(256, 256)

    # Apply a Gaussian filter with sigma = 2
    filtered_image = multidimensional_gaussian_filter(image, sigma=2)

    # Display the original and filtered images
    import matplotlib.pyplot as plt
    plt.subplot(121)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.subplot(122)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.show()
