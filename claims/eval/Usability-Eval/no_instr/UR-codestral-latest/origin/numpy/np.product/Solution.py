import numpy as np

# Create a numpy array for demonstration
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate the product of array elements over axis 0
product_axis_0 = np.prod(arr, axis=0)

# Calculate the product of array elements over axis 1
product_axis_1 = np.prod(arr, axis=1)

print("Product over axis 0: ", product_axis_0)
print("Product over axis 1: ", product_axis_1)
