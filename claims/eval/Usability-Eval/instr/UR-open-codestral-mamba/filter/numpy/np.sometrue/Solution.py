import numpy as np

# Generate a boolean numpy array
my_array = np.array([1, 2, 3, 0, 5]) > 0

# Test whether any array element along a given axis evaluates to True.
result = np.any(my_array)

print(result)
