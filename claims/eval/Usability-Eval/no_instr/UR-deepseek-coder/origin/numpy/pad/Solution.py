import numpy as np

def pad_array(arr, pad_width, mode='constant', constant_values=0):
    """
    Pad an array with specified width and mode.

    Parameters:
    arr (numpy.ndarray): The input array to be padded.
    pad_width (int or tuple): The number of values padded to the edges of each axis.
    mode (str): The mode of padding. Default is 'constant'.
    constant_values (int or tuple): The values to set the padded values for each axis. Default is 0.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(arr, pad_width, mode=mode, constant_values=constant_values)

# Example usage:
# arr = np.array([[1, 2], [3, 4]])
# padded_arr = pad_array(arr, pad_width=((1, 1), (2, 2)), mode='constant', constant_values=0)
# print(padded_arr)
