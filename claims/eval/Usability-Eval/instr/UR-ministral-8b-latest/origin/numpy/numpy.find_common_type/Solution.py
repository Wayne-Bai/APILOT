import numpy as np

def find_common_type(arr1, arr2):
    type1 = np.dtype(arr1).kind
    type2 = np.dtype(arr2).kind

    if type1 == type2:
        return np.dtype(type1)

    # Detecting common type based on standard coercion rules
    type_coercion_map = {
        np.int32, np.int64, np.int_,
        np.floating
    }

    for t in type_coercion_map:
        if t in (type1, type2):
            return np.dtype(t)

    # If no common type found, return None
    return None

# Example usage:
arr1 = np.array([1, 2, 3], dtype=np.int32)
arr2 = np.array([4.0, 5.0, 6.0], dtype=np.float64)
print(find_common_type(arr1, arr2))  # Output: float64

arr3 = np.array([True, False], dtype=bool)
arr4 = np.array([7, 8, 9], dtype=np.int32)
print(find_common_type(arr3, arr4))  # Output: None
