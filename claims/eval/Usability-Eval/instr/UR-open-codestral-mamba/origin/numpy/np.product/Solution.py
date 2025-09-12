# Start with importing the numpy library
import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4])

# Use numpy's prod() function to return the product of array elements over a given axis
# For getting product over all the elements in the array, the default axis=None can be used
print(np.prod(arr))

# For getting product over a specific axis, you can pass axis as arguments. For example, to get product of each row in a 2D array, use axis=1
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.prod(arr_2d, axis=1))

# Note that the prod() function gives the product of all array elements if axis=None
print(np.prod(arr_2d))
