import numpy as np

def find_unique_elements(array, return_index=False, return_inverse=False):
    """
    Find the unique elements of an array.

    Args:
        array (numpy.ndarray): Input array.
        return_index (bool, optional): If True, returns the indices of the 
            input array that produce the unique elements. Defaults to False.
        return_inverse (bool, optional): If True, returns the indices of the
            unique elements that appear in the input array. Defaults to False.

    Returns:
        tuple: A tuple containing the sorted unique elements, and optionally,
            the indices of the input array that produce the unique elements,
            and the indices of the unique elements that appear in the input array.
    """
    unique_elements, inverse_indices, counts = np.unique(array, return_inverse=True, return_counts=True)
    sorted_unique_elements = npArgsort(unique_elements)

    if return_index:
        indices = np.searchsorted(unique_elements, array)
        return (sorted_unique_elements, indices)
    elif return_inverse:
        return (sorted_unique_elements, inverse_indices)
    else:
        return sorted_unique_elements

# Example usage:
array = np.array([1, 2, 3, 2, 1, 4, 5, 3, 6, 7, 8, 9, 0, 4, 5])
print(find_unique_elements(array))
print(find_unique_elements(array, return_index=True))
print(find_unique_elements(array, return_inverse=True))
