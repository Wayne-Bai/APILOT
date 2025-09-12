
import numpy as np

def test_all(arr, axis=None):
    """
    Test whether all array elements along a given axis evaluate to True.

    Parameters
    ----------
    arr : ndarray
        The input array.
    axis : int or None, optional
        Axis along which the test is performed. If None, the test is performed on the flattened array. Default: None.

    Returns
    -------
    bool
        Whether all elements along the specified axis evaluate to True.

    See Also
    --------
    numpy.all : Function that tests whether all array elements along a given axis evaluate to True.

    Examples
    --------
    >>> arr = np.array([[True, False], [True, True]])
    >>> test_all(arr)
    False
    >>> test_all(arr, axis=0)
    array([ True, False])
    >>> test_all(arr, axis=1)
    array([False,  True])
    """
    return np.all(arr, axis=axis)
