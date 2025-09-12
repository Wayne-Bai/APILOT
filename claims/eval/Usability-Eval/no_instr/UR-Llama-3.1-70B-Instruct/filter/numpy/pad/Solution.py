import numpy as np

def pad_array(array, pad_width, mode='constant', constant_values=0):
    """
    Pads an array.

    Args:
    array (numpy.ndarray): Input array.
    pad_width (tuple or int): Number of values padded to the edges of each axis.
    mode (str): Padding mode. Options: 'constant', 'edge', 'linear_ramp','maximum','mean','median','minimum','reflect','symmetric', 'wrap'.
    constant_values (int, tuple): Values used in 'constant' mode.

    Returns:
    numpy.ndarray: Padded array.
    """

    return np.pad(array, pad_width, mode=mode, constant_values=constant_values)


# example usage
array = np.arange(8).reshape(2, 4)
print("Original array:")
print(array)

padded_array = pad_array(array, ((1, 1), (1, 1)))
print("\nPadded array:")
print(padded_array)


# edge padding
array = np.arange(8).reshape(2, 4)
print("\n\nOriginal array:")
print(array)

padded_array = pad_array(array, ((1, 1), (1, 1)), mode='edge')
print("\nPadded array (edge mode):")
print(padded_array)


# constant padding with custom values
array = np.arange(8).reshape(2, 4)
print("\n\nOriginal array:")
print(array)

padded_array = pad_array(array, ((1, 1), (1, 1)), mode='constant', constant_values=100)
print("\nPadded array (constant mode with custom values):")
print(padded_array)
