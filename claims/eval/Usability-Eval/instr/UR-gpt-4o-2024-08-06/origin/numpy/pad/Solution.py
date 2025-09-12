import numpy as np

def pad_array(arr, pad_width, mode='constant', **kwargs):
    """
    Pads an array with the specified padding width and mode.

    Parameters:
    arr (numpy.ndarray): The array to pad.
    pad_width (int or sequence of ints): Number of values padded to the edges of each axis.
    mode (str): Padding mode, options are 'constant', 'edge', 'linear_ramp', 'maximum', 
                'mean', 'median', 'minimum', 'reflect', 'symmetric', 'wrap'.
    **kwargs: Additional keyword arguments to be passed to numpy.pad.

    Returns:
    numpy.ndarray: The padded array.
    """
    return np.pad(arr, pad_width, mode=mode, **kwargs)

# Example usage
array = np.array([[1, 2], [3, 4]])
padded_array = pad_array(array, pad_width=1, mode='constant', constant_values=0)
print(padded_array)
