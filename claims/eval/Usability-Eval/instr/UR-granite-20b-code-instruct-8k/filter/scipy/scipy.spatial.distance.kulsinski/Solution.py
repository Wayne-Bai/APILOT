import numpy as np
from scipy.spatial import distance

arr1 = np.array([True, True, False, True, False])
arr2 = np.array([True, False, True, False, True])

result = distance.kulsinski(arr1, arr2)
print(result)
