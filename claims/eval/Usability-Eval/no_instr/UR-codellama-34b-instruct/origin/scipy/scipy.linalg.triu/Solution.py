import numpy as np

def zero_below_kth(arr, k):
    """
    Function to make a copy of a matrix with elements below the kth diagonal zeroed.
    :param arr: The input array
    :type arr: numpy.ndarray
    :param k: The diagonal to zero below
    :type k: int
    :return: The modified array with elements below the kth diagonal zeroed
    :rtype: numpy.ndarray
    """
    result = np.zeros(arr.shape, dtype=arr.dtype)
    for i in range(k):
        result[i, i:] = arr[i, i:]
    return result
