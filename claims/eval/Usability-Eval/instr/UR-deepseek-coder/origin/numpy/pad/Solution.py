import numpy as np

def pad_array(array, pad_width, mode='constant', constant_values=0):
    """
    Pad an array using numpy.

    Parameters:
    array (numpy.ndarray): The array to be padded.
    pad_width (tuple of ints): Number of values padded to the edges of each axis.
    mode (str): Padding mode. Default is 'constant'.
    constant_values (int or tuple): Used in 'constant' mode as the value to set the padded values for each axis.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(array, pad_width, mode=mode, constant_values=constant_values)

# Example usage:
array = np.array([[1, 2], [3, 4]])
padded_array = pad_array(array, ((1, 1), (2, 2)), mode='constant', constant_values=0)
print(padded_array)
