import numpy as np

# Create arrays with different data types
arr1 = np.array([1, 2, 3])
arr2 = np.array([4.0, 5.0, 6.0])
arr3 = np.array(['a', 'b', 'c'])

# Determine the common data type
common_type = np.common_type(arr1, arr2, arr3)

print("Common data type:", common_type)
