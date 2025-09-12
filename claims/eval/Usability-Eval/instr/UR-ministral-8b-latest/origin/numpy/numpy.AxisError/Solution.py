import numpy as np

def safe_array_creation(input_array, axis):
    try:
        # Try to create the array with the specified axis
        output_array = np.array(input_array, axis=axis)
    except (ValueError, IndexError) as e:
        # Catch ValueError and IndexError and re-raise as an AxisError for compatibility with older numpy versions
        raise AxisError(f"Axis supplied was invalid: {axis}")

# Example usage
try:
    array = [1, 2, 3, 4]
    safe_array_creation(array, 4)
except AxisError as e:
    print(e)
