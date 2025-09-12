import numpy as np
# Stack arrays in sequence vertically (row wise).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.vstack([arr1, arr2])
print(result)
