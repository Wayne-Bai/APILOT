
import numpy as np

# Define the input array
a = np.array([[1, 2], [3, 4]])

# Calculate the product of array elements over axis=0 (rows)
b = np.prod(a, axis=0)
print(b)
