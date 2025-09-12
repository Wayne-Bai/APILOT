
import numpy as np
from scipy import signal

# Generate a 1-D Gaussian filter using the GaussLaguerre kernel
def gaussian_filter(input_array, sigma):
    # Compute the size of the filter
    n = 2 * int(np.ceil(sigma * np.sqrt(-2 * np.log(0.5)))) + 1

    # Generate the weights for the filter
    weights = signal.gauss_laguerre(n, sigma)

    # Normalize the weights to sum to 1
    weights /= weights.sum()

    # Create the 1-D Gaussian filter
    gaussian_filter = np.ones(input_array.shape[0], dtype=np.float32)
    for i in range(n):
        gaussian_filter *= weights[i]

    return gaussian_filter
