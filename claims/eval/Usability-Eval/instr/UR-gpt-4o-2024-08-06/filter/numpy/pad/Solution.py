import numpy as np

def pad_array(array, pad_width, constant_values=0):
    """
    Pads an array with specified width and constant values.
    
    Parameters:
    array (numpy.ndarray): An array to be padded.
    pad_width (int) or ((int, int), ...): Number of values padded to the edges of each axis.
    constant_values (int, float, or sequence): The values to set the padded values for each axis.

    Returns:
    numpy.ndarray: The padded array.
    """
    padded_array = np.pad(array, pad_width, mode='constant', constant_values=constant_values)
    return padded_array

# Example usage:
original_array = np.array([[1, 2], [3, 4]])
padded_array = pad_array(original_array, pad_width=1, constant_values=0)
print(padded_array)
