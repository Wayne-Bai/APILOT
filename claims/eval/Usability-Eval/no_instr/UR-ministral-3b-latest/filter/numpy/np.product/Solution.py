import numpy as np
# Initializing numpy array
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculating the product of array elements over a given axis
product = np.prod(arr, axis=0)

print("Product along axis 0:", product)
