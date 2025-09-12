
import numpy as np

# create a sequence of arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

# join the arrays along a new axis
result = np.stack((a, b, c), axis=1)

print(result)
