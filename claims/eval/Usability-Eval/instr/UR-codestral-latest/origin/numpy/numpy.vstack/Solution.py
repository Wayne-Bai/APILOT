import numpy as np

# Let's assume we have two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# To stack arrays in sequence vertically (row wise)
stacked_array = np.vstack((array1, array2))

print(stacked_array)
