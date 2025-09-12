import numpy as np

def determine_common_type(*args):
    # Check for integer types
    int_types = [arg.dtype for arg in args if arg.dtype.kind == 'i']
    if int_types:
        if set(int_types) == {np.int64}:
            return np.int64
        elif set(int_types) == {np.int32}:
            return np.int32
        elif set(int_types) == {np.int8, np.int16, np.int32, np.int64}:
            return np.int32
        else:
            return np.result_type(*int_types)

    # Check for float types
    float_types = [arg.dtype for arg in args if arg.dtype.kind == 'f']
    if float_types:
        if set(float_types) == {np.float64}:
            return np.float64
        elif set(float_types) == {np.float32}:
            return np.float32
        elif set(float_types) == {np.float16, np.float32, np.float64}:
            return np.float32
        else:
            return np.result_type(*float_types)

    # Check for complex types
    complex_types = [arg.dtype for arg in args if arg.dtype.kind == 'c']
    if complex_types:
        return np.complex128

    # If no types are found, use np.object_
    return np.object_

# Test the function
arr1 = np.array([1, 2, 3], dtype=np.int32)
arr2 = np.array([4, 5, 6], dtype=np.int16)
arr3 = np.array([1.1, 2.2, 3.3], dtype=np.float64)
arr4 = np.array([1 + 1j, 2 + 2j, 3 + 3j], dtype=np.complex64)

print(determine_common_type(arr1, arr2))
print(determine_common_type(arr3))
print(determine_common_type(arr4))
