import numpy as np
from scipy.ndimage import gaussian_filter

def apply_multidimensional_gaussian_filter(input_array, sigma):
    """
    Applies a multidimensional Gaussian filter to the input array.
    
    Parameters:
    input_array (np.ndarray): The input array to which the Gaussian filter will be applied.
    sigma (float or sequence of floats): Standard deviation for Gaussian kernel.
    
    Returns:
    np.ndarray: The filtered array.
    """
    return gaussian_filter(input_array, sigma)

# Example usage
if __name__ == "__main__":
    # Create a sample 2D array (image)
    input_array = np.random.rand(100, 100)
    
    # Apply the Gaussian filter with a standard deviation of 2
    filtered_array = apply_multidimensional_gaussian_filter(input_array, sigma=2)
    
    print("Filtered Array:")
    print(filtered_array)
