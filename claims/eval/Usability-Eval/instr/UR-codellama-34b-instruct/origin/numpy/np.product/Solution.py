import numpy as np

def array_product(arr, axis=None):
    """
    Calculate the product of array elements over a given axis.

    Parameters
    ----------
    arr : numpy array
        The input array.
    axis : int or tuple of ints, optional
        Axis or axes along which the product is calculated. The default
        is to calculate the product over all elements.

    Returns
    -------
    prod : numpy array
        The product of array elements over the given axis.
    """
    if axis is None:
        return np.prod(arr)
    else:
        return np.prod(arr, axis=axis)
