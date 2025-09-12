import numpy as np

def common_type(arrays):
    """
    Determine common type following standard coercion rules.

    Parameters:
    arrays (list of arrays): Input arrays

    Returns:
    type: Common type of the input arrays
    """
    type_list = [array.dtype.type if isinstance(array, np.ndarray) else type(array[0]) for array in arrays]
    return np.find_common_type(type_list, [])

# Example usage:
arrays = [np.array([1, 2, 3]), np.array([1.0, 2.0, 3.0]), [1, 2, 3]]
print(common_type(arrays))
