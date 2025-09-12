
import numpy as np

def pad_array(array, pad_width, mode='constant', constant_values=0):
    """
    Pad an array with specified pad_width and constant values.
    
    Parameters
    ----------
    array : numpy.ndarray
        The input array to be padded.
    pad_width : int or tuple of int
        The number of values padded to the edges of each axis.
        If a single int is given, it is used for all axes.
        If a tuple of int is given, it must have the same length as the number of axes.
    mode : {'constant', 'edge', 'wrap'}, optional
        The type of padding to be applied. Default is 'constant'.
        'constant' pads with a constant value.
        'edge' pads with the edge values of the array.
        'wrap' pads with the wrap of the array.
    constant_values : scalar or tuple, optional
        The values to set the padded values for each axis.
        If a single value is given, it is used for all axes.
        If a tuple of values is given, it must have the same length as the number of axes.
        Default is 0.
        
    Returns
    -------
    numpy.ndarray
        The padded array.
    """
    return np.pad(array, pad_width, mode=mode, constant_values=constant_values)
