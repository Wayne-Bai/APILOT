import numpy as np

def check_axis(arr, axis):
    try:
        # Attempt to perform an operation that requires a valid axis
        np.sum(arr, axis=axis)
    except np.AxisError as e:
        print(f"AxisError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
arr = np.array([[1, 2, 3], [4, 5, 6]])
check_axis(arr, axis=2)  # This will raise an AxisError
