import numpy as np

# Create a sample 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Print the original array
print("Original Array:")
print(arr)

# Calculate the product of array elements over a given axis
# In this case, we want to calculate the product along axis=1 (i.e., each row)
product_axis_1 = np.prod(arr, axis=1)

# Print the result
print("\nProduct along axis=1 (each row):")
print(product_axis_1)

# Calculate the product along axis=0 (i.e., each column)
product_axis_0 = np.prod(arr, axis=0)

# Print the result
print("\nProduct along axis=0 (each column):")
print(product_axis_0)
