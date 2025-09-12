import numpy as np

def determine_common_type(*arrays):
    """
    Determine the common type following standard coercion rules for the given arrays.

    Parameters:
    *arrays (np.ndarray): Variable number of numpy arrays.

    Returns:
    np.dtype: The common type following standard coercion rules.
    """
    if not arrays:
        raise ValueError("At least one array must be provided.")

    # Start with the type of the first array
    common_type = arrays[0].dtype

    # Iterate over the remaining arrays to determine the common type
    for array in arrays[1:]:
        common_type = np.promote_types(common_type, array.dtype)

    return common_type

# Example usage:
# array1 = np.array([1, 2, 3], dtype=np.int32)
# array2 = np.array([4.0, 5.0, 6.0], dtype=np.float64)
# common_type = determine_common_type(array1, array2)
# print(common_type)  # Output: dtype('float64')
