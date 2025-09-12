import numpy as np

# Define the function to check if all elements evaluate to True
def all_vals_true(arr):
    """Check if all elements in the array along a given axis evaluate to True"""
    return np.all(arr)

# Example usage
arr = np.array([[True, True], [False, True]])
result = all_vals_true(arr)
print("All elements along the specified axis evaluate to True:", result)
