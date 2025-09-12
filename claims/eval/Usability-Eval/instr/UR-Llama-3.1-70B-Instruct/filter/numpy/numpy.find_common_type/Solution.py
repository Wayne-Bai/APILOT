import numpy as np

def find_common_type(arrays):
    """
    Determine the common type of a list of arrays following standard coercion rules.
    
    Parameters:
    arrays (list): A list of numpy arrays
    
    Returns:
    type: The common type of the input arrays
    """
    types = [arr.dtype.type for arr in arrays if arr.dtype.kind!= 'O']
    types = list(set(types))  # remove duplicates

    if not types:
        return np.object_

    # Standard coercion rules
    integer_types = [np.int0, np.int8, np.int16, np.int32, np.int64]
    unsigned_types = [np.uint8, np.uint16, np.uint32, np.uint64]
    float_types = [np.float16, np.float32, np.float64, np.longdouble]

    type_map = {np.dtype(t).kind: t for t in types}

    if 'b' in type_map:  # boolean
        return type_map['b']

    if 'i' in type_map and 'u' in type_map:
        return np.float64
    elif 'i' in type_map:
        return np.int64
    elif 'u' in type_map:
        return np.uint64

    if 'f' in type_map:
        return np.float64

    if 'c' in type_map:
        return np.cdouble

    if 'O' in type_map:
        return np.object_

    # Fallback to the first type if none of the above rules matched
    return types[0]

# Example usage:
arrays = [np.array([1, 2, 3]), np.array([1.5, 2.5, 3.5])]
common_type = find_common_type(arrays)
print(common_type)
