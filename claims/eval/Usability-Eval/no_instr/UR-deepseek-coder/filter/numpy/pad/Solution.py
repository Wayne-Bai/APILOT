import numpy as np

def pad_array(array, pad_width, mode='constant', constant_values=0):
    """
    Pad an array using numpy.

    Parameters:
    array (numpy.ndarray): The input array to be padded.
    pad_width (tuple of tuples): Number of values padded to the edges of each axis.
                                 ((before_1, after_1), ... (before_N, after_N))
    mode (str): Padding mode. One of {'constant', 'edge', 'linear_ramp', 'maximum', 'mean', 'median', 'minimum', 'reflect', 'symmetric', 'wrap'}.
    constant_values (scalar or array-like): Used in 'constant' mode as the value to fill the padding areas.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(array, pad_width, mode=mode, constant_values=constant_values)

# Example usage:
# array = np.array([[1, 2], [3, 4]])
# padded_array = pad_array(array, ((1, 1), (2, 2)), mode='constant', constant_values=0)
# print(padded_array)
