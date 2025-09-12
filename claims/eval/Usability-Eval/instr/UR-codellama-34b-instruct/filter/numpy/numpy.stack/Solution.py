
import numpy as np

# Define the sequences of arrays to be joined
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

# Use np.stack to join the sequences along a new axis
joined_array = np.stack((a, b, c), axis=0)

print(joined_array)
