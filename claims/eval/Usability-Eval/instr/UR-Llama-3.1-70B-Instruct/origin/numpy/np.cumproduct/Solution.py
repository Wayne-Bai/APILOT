import numpy as np

# Create a 2D numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Use np.cumprod() function to calculate the cumulative product
# along the given axis (0 for columns, 1 for rows)
cumulative_product_axis_0 = np.cumprod(array, axis=0)
cumulative_product_axis_1 = np.cumprod(array, axis=1)

# Print the results
print("Original array:")
print(array)

print("\nCumulative product along axis 0 (columns):")
print(cumulative_product_axis_0)

print("\nCumulative product along axis 1 (rows):")
print(cumulative_product_axis_1)
