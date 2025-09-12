import numpy as np

def array_product(axis):
    # Create a sample 2D array for demonstration
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Compute the product of array elements over the specified axis
    product = np.product(arr, axis=axis)
    return product

# Example usage:
result = array_product(0)
print("Product along axis 0:", result)

result = array_product(1)
print("Product along axis 1:", result)
