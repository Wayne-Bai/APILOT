import numpy as np

def pad_array(array, pad_width, mode='constant'):
    """
    Pad an array with a specified width using a specified mode.

    Parameters:
    array (numpy.ndarray): The array to be padded.
    pad_width (int or tuple of ints): The number of values to add at the start and end of each axis.
    mode (str, optional): The padding mode. Can be 'constant', 'edge', or 'symmetric'. Defaults to 'constant'.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(array, pad_width, mode)
