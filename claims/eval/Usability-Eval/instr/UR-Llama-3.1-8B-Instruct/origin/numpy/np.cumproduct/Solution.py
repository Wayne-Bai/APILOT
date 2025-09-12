import numpy as np

# Create a sample 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Return the cumulative product of elements along a given axis
def cumulative_product(array, axis):
    return np.cumprod(array, axis=axis)

# Print the original array
print("Original Array:")
print(array)

# Calculate the cumulative product along axis=0
print("\nCumulative Product along axis 0:")
print(cumulative_product(array, axis=0))

# Calculate the cumulative product along axis=1
print("\nCumulative Product along axis 1:")
print(cumulative_product(array, axis=1))
