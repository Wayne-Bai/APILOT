import numpy as np

def pad_array(arr, pad_width):
    """
    Pad an array with specified padding width.

    Parameters:
    arr (numpy.ndarray): The input array to pad.
    pad_width (int or tuple of int): The width of each side to pad. If an int is provided, that many elements will be added to both ends of the array. If a tuple is provided, the first element specifies the number of elements to add to the beginning and the second element specifies the number to add to the end.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(arr, pad_width, mode='edge')

# Example usage:
input_array = np.array([1, 2, 3])
padding_size = (2, 3)

padded_array = pad_array(input_array, padding_size)
print(padded_array)
