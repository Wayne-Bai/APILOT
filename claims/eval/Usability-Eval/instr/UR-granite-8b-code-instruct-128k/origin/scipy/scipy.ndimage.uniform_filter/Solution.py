from scipy import ndimage as nd

def uniform_filter(input, size=3):
    """
    Apply a uniform filter to the input array.

    Parameters:
    input (ndarray): The input array to filter.
    size (int or tuple of int): The size of the filter.

    Returns:
    ndarray: The filtered output array.

    Examples:
    >>> a = np.array([[0,1,2],[3,4,5],[6,7,8]])
    >>> uniform_filter(a, size=3)
    array([[2. 3. 4.]
           [4. 5. 6.]
           [6. 7. 8.]])
    """
    return nd.uniform_filter(input, size=size)
