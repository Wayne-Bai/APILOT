import numpy as np

# Custom function to demonstrate raising AxisError
def example_function(arr, axis):
    try:
        # Attempt to sum over the specified axis
        result = np.sum(arr, axis=axis)
        return result
    except ValueError as e:
        # Handle ValueError specifically
        print(f"ValueError encountered: {e}")
    except IndexError as e:
        # Handle IndexError specifically
        print(f"IndexError encountered: {e}")
    except np.AxisError as e:
        # Handle AxisError specifically
        print(f"AxisError: {e}")

# Example use case
if __name__ == "__main__":
    # Creating a 2D array
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # Valid axis
    print("For valid axis 1:", example_function(arr, 1))

    # Invalid axis that triggers AxisError
    example_function(arr, 3)  # This will raise an AxisError
