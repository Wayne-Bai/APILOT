
import numpy as np

# Example data
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

# Join the arrays along a new axis
joined_arr = np.concatenate((a, b, c), axis=0)
print(joined_arr)
