import numpy as np

# Assuming 'arr' is the input array
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Return a sorted copy of the array
sorted_arr = np.copy(arr)
np.sort(sorted_arr)

print(sorted_arr)
