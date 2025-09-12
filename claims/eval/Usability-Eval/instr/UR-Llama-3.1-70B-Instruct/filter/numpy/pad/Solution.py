import numpy as np

def pad_array(array, pad_value, pad_width):
    """
    Pad an array with a specified value.

    Parameters:
    array (numpy.ndarray): The input array to be padded.
    pad_value (float): The value used to pad the array.
    pad_width (int or tuple): The number of values to pad along each axis.

    Returns:
    padded_array (numpy.ndarray): The padded array.
    """
    # Check if the array is a numpy array
    if not isinstance(array, np.ndarray):
        array = np.array(array)

    # Pad the array
    padded_array = np.pad(array, pad_width, mode='constant', constant_values=pad_value)

    return padded_array

# Example usage
if __name__ == "__main__":
    # Create a sample array
    array = np.array([[1, 2, 3], [4, 5, 6]])

    # Pad the array with a value of 0 and a width of 1
    padded_array = pad_array(array, 0, 1)

    # Print the original and padded arrays
    print("Original Array:")
    print(array)
    print("\nPadded Array:")
    print(padded_array)
