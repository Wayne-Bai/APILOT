
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1.5, 2.5, 3.5])
arr3 = np.array(['a', 'b', 'c'])

common_type = np.result_type(arr1, arr2, arr3)

print("Common type following standard coercion rules:", common_type)
