import numpy as np

class AxisError(ValueError, IndexError):
    """Raised when an axis parameter is specified that is out of range"""
    pass

def validate_axis(array, axis):
    """Check if axis is within valid range for given array"""
    if not isinstance(array, np.ndarray):
        raise TypeError("Input is not a numpy array")
    if axis < 0 or axis >= array.ndim:
        raise AxisError("Axis {} is out of range for array with {} dimensions".format(axis, array.ndim))

# Example usage:
try:
    array = np.array([[1, 2], [3, 4]])
    validate_axis(array, 2)  # Should raise AxisError
except AxisError as e:
    print(e)

try:
    validate_axis(array, 0)
except AxisError as e:
    print(e)
