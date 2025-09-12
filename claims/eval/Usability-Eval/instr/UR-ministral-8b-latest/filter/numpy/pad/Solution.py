import numpy as np

def pad_array(array, pad_height, pad_width, pad_value=0):
    """
    Pad an array with the specified height and width using the given pad value.

    Parameters:
    - array: np.ndarray, input array to pad
    - pad_height: int, number of rows to pad
    - pad_width: int, number of columns to pad
    - pad_value: float, value to pad with

    Returns:
    - np.ndarray, the padded array
    """
    padded_array = np.pad(array, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=pad_value)
    return padded_array

# Example usage
original_array = np.array([[1, 2, 3], [4, 5, 6]])
padded_array = pad_array(original_array, 1, 1)
print(padded_array)
