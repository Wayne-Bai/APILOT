from scipy import signal
import numpy as np

def median_filter(data, size):
    """Calculate a multidimensional median filter.

    Args:
    data (numpy.ndarray): The input image.
    size (int): The size of the median filter.

    Returns:
    smoothed_data (numpy.ndarray): The smoothed output image.
    """

    # Define the size of the volume after performing the median filter
    size_after_filter = np.array(data.shape) - size + 1

    # Prepare the shape of the structuring element
    struct_elem = np.ones(size, dtype=bool)

    # Apply median filter
    smoothed_data = signal.medfilt(data, struct_elem.shape)

    return smoothed_data
