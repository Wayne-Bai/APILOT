import numpy as np

# Define two arrays with different data types
arr1 = np.array([1, 2, 3])
arr2 = np.array([4.5, 5.6, 6.7])

# Determine the common data type following standard coercion rules
common_type = np.common_type(arr1, arr2)

print("The common data type is:", common_type)
