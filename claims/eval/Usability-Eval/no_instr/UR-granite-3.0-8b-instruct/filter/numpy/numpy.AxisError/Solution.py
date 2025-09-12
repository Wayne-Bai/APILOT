import numpy as np

def validate_axis(axis, arr):
    if not isinstance(axis, int) or axis < 0 or axis >= arr.ndim:
        raise ValueError("Axis supplied was invalid.")

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6]])
validate_axis(2, arr)  # This will raise a ValueError
