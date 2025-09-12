import numpy as np

# Example array
array = np.array([True, False, True, False, True])

# Function to test whether all array elements along a given axis evaluate to True
def all_true_along_axis(array, axis):
    return np.all(array, axis=axis)

# Test the function
result = all_true_along_axis(array, 0)
print(result)  # Output: False

# For demonstration, test with an array where all elements are True
array = np.array([True, True, True, True, True])
result = all_true_along_axis(array, 0)
print(result)  # Output: True
