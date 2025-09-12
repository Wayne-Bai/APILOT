import numpy as np

def pad_array(arr, pad_width, mode='constant', constant_values=0):
    """
    Pad an array with specified width and mode.

    Parameters:
    arr (numpy.ndarray): The input array to be padded.
    pad_width (tuple of ints): Number of values padded to the edges of each axis.
    mode (str): Padding mode, default is 'constant'.
    constant_values (int or tuple): Used in 'constant' mode as the value to fill the padding.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(arr, pad_width, mode=mode, constant_values=constant_values)

# Example usage:
arr = np.array([[1, 2], [3, 4]])
padded_arr = pad_array(arr, ((1, 1), (2, 2)), mode='constant', constant_values=0)
print(padded_arr)
