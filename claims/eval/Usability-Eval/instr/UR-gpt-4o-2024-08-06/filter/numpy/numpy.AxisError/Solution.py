import numpy as np

def check_axis_error(array, axis):
    try:
        # Attempting to sum along an invalid axis to trigger an AxisError
        np.sum(array, axis=axis)
    except np.AxisError as e:
        print(f"AxisError: {e}")

# Example usage
# Creating an example 2D numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Checking for axis errors
check_axis_error(array, axis=2)  # This should raise an AxisError as only axis 0 and 1 are valid
