import numpy as np

def pad_array(array, pad_width, pad_value):
    """
    Pad a given 1D numpy array with a specified padding width and value.

    Parameters:
    array (np.ndarray): The 1D numpy array to be padded.
    pad_width (int): The amount of padding to add to both ends of the array.
    pad_value (int, float, or None): The value to use for padding.

    Returns:
    np.ndarray: The padded numpy array.
    """
    padded_array = np.pad(array, (pad_width, pad_width), mode='constant', constant_values=pad_value)
    return padded_array

# Example usage
array = np.array([1, 2, 3])
pad_width = 2
pad_value = 0
padded_array = pad_array(array, pad_width, pad_value)
print(padded_array)
