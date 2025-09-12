import numpy as np

def safe_axis_operation(arr, axis):
    try:
        return np.sum(arr, axis=axis)
    except (ValueError, IndexError):
        print("Axis supplied was invalid.")
        return None

# Example usage:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(safe_axis_operation(arr, 3))  # This will print: Axis supplied was invalid.
print(safe_axis_operation(arr, 0))  # This will print: [ 15 15 15]
