from scipy.spatial.distance import kulsinski
import numpy as np

# Solution 1
array1 = np.array([True, False, True, True])
array2 = np.array([False, True, True, False])
diss_1 = kulsinski(array1, array2)
print(diss_1)

# Solution 2
array1 = np.array([True, True, False, True])
array2 = np.array([True, False, True, True])
diss_2 = kulsinski(array1, array2)
print(diss_2)

# Solution 3
array1 = np.array([False, False, True, False])
array2 = np.array([True, False, False, True])
diss_3 = kulsinski(array1, array2)
print(diss_3)

# Solution 4
array1 = np.array([True, False, False, False])
array2 = np.array([False, False, True, False])
diss_4 = kulsinski(array1, array2)
print(diss_4)

# Solution 5
array1 = np.array([False, True, False, True])
array2 = np.array([False, True, True, False])
diss_5 = kulsinski(array1, array2)
print(diss_5)

# Solution 6
array1 = np.array([True, True, True, False])
array2 = np.array([True, True, False, True])
diss_6 = kulsinski(array1, array2)
print(diss_6)

# Solution 7
array1 = np.array([False, False, False, True])
array2 = np.array([True, False, True, False])
diss_7 = kulsinski(array1, array2)
print(diss_7)

# Solution 8
array1 = np.array([True, False, True, False])
array2 = np.array([False, True, False, True])
diss_8 = kulsinski(array1, array2)
print(diss_8)

# Solution 9
array1 = np.array([True, True, False, False])
array2 = np.array([False, False, True, True])
diss_9 = kulsinski(array1, array2)
print(diss_9)

# Solution 10
array1 = np.array([False, False, True, True])
array2 = np.array([True, True, False, False])
diss_10 = kulsinski(array1, array2)
print(diss_10)
