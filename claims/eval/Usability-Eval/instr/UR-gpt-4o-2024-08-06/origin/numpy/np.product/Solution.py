import numpy as np

def product_of_elements(array, axis=None):
    """
    Return the product of array elements over a given axis.
    
    Parameters:
    array (ndarray): Input array.
    axis (int, optional): Axis along which the product is computed. 
                          By default, computes the product of all elements.
    
    Returns:
    numpy.ndarray or numpy.scalar: The product of elements.
    """
    return np.prod(array, axis=axis)

# Example usage:
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = product_of_elements(arr, axis=0)
print("Product along axis 0:", result)

result = product_of_elements(arr, axis=1)
print("Product along axis 1:", result)

result = product_of_elements(arr)
print("Product of all elements:", result)
