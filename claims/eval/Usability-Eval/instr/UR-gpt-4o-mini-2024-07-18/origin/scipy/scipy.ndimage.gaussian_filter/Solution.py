import numpy as np
from scipy.ndimage import gaussian_filter

def apply_gaussian_filter(image, sigma):
    """
    Apply a multidimensional Gaussian filter to an image.

    Parameters:
    image (ndarray): Input image array.
    sigma (float or tuple): Standard deviation for Gaussian kernel. 
                            If a float, the same value is used for all dimensions. 
                            If a tuple, it should have the same number of elements as dimensions of the image.

    Returns:
    ndarray: The filtered image.
    """
    return gaussian_filter(image, sigma)

# Example usage
if __name__ == "__main__":
    # Create a sample 2D image
    sample_image = np.random.rand(100, 100)
    
    # Apply Gaussian filter with a sigma of 2
    filtered_image = apply_gaussian_filter(sample_image, sigma=2)
