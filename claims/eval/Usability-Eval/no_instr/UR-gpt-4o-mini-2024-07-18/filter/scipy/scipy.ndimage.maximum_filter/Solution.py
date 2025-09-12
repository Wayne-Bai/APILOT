import numpy as np
from scipy.ndimage import maximum_filter

def multidimensional_maximum_filter(input_array, footprint=None, mode='reflect', cval=0.0):
    """
    Apply a multidimensional maximum filter to the input array.

    Parameters:
    - input_array: The input array to be processed.
    - footprint: The structure used to determine the neighborhood.
    - mode: The mode for handling borders.
    - cval: The constant value used in 'constant' mode.

    Returns:
    - The filtered array with maximum values.
    """
    return maximum_filter(input_array, footprint=footprint, mode=mode, cval=cval)

# Example usage
if __name__ == "__main__":
    # Create a sample 2D input array
    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    # Define the footprint, if needed (e.g., a 3x3 square)
    footprint = np.ones((3, 3))

    # Apply the multidimensional maximum filter
    result = multidimensional_maximum_filter(data, footprint=footprint)

    print("Input Array:")
    print(data)
    print("\nFiltered Array:")
    print(result)
