import numpy as np

def determine_common_type(arrays):
    # Flatten arrays to determine a single common data type
    flat_array = np.concatenate([np.ravel(a) for a in arrays])
    common_type = flat_array.dtype

    # Create a list of unique types in the flattened array
    unique_types = set(flat_array[i].dtype for i in range(flat_array.size))

    # Determine the common type
    if np.bool_ in unique_types and len(unique_types) > 1:
        unique_types.remove(np.bool_)

    if len(unique_types) == 1:
        return list(unique_types)[0]
    
    # Manually determine the common type based on coercion rules
    if np.int_ in unique_types and np.float_ in unique_types:
        common_type = np.float_
    elif any(issubclass(t.type, np.complexfloating) for t in unique_types):
        common_type = np.complex_
    elif any(issubclass(t.type, np.float_) for t in unique_types):
        common_type = np.float_
    else:
        common_type = np.int_

    return common_type

# Example usage
array1 = np.array([1, 2, 3])
array2 = np.array([4.5, 5.5])
array3 = np.array([6j, 7j])

common_type = determine_common_type([array1, array2, array3])
print(f"The common data type is: {common_type}")
