import numpy as np
from scipy.ndimage import gaussian_filter

def multidimensional_gaussian_filter(data, sigma):
    """
    Applies a multidimensional Gaussian filter to the input data.

    Parameters:
    data (numpy array): The input data to be filtered.
    sigma (float or tuple of floats): The standard deviation(s) of the Gaussian filter.

    Returns:
    filtered_data (numpy array): The filtered data.
    """
    # Apply the Gaussian filter
    filtered_data = gaussian_filter(data, sigma)

    return filtered_data

# Example usage:
if __name__ == "__main__":
    # Create a sample 3D dataset
    data = np.random.rand(10, 10, 10)

    # Define the standard deviation(s) of the Gaussian filter
    sigma = (1.0, 1.0, 1.0)

    # Apply the multidimensional Gaussian filter
    filtered_data = multidimensional_gaussian_filter(data, sigma)

    # Print the filtered data
    print(filtered_data)
