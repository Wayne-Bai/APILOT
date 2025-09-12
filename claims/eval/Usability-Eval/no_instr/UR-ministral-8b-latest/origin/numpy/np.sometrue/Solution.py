import numpy as np

# Example array for testing
array = np.array([False, True, False, True, False])

# Function to check if any element along axis evaluates to True
def any_along_axis(array, axis):
    return np.any(array, axis=axis)

# Test the function
result = any_along_axis(array, 0)
print(f"Any element along axis 0 evaluates to True: {result}")

# You can also test it with other axes or different arrays
