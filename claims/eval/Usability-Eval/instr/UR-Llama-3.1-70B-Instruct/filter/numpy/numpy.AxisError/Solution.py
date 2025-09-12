import numpy as np

class CustomAxisError(Exception):
    """Raised when an axis parameter is specified that is larger than the number of array dimensions."""
    pass

def validate_axis(array, axis):
    """Validate the axis parameter."""
    if axis >= array.ndim or axis < -array.ndim:
        raise CustomAxisError("Axis supplied was invalid")

def main():
    try:
        # Create a 2D numpy array
        array = np.array([[1, 2], [3, 4]])

        # Test invalid axis
        validate_axis(array, 2)
    except CustomAxisError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
