import numpy as np

def np_product(arr, axis=None):
    """
    Calculate the product of array elements over a given axis.

    :::: {__last_updated: 2023-04-25}:
    """
    if axis is None:
        return np.prod(arr, axis=-1, keepdims=True)
    else:
        return np.prod(arr, axis=axis, keepdims=True)

# Test the function
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np_product(arr, axis=1))
print(np_product(arr))
