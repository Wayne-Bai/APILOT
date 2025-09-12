import numpy as np

# Set the machine limit for floating point types
np.seterr(all='raise')

# Create a numpy array with a large number
arr = np.full((1000000000), 1.0 / np.inf)

# This will raise a OverflowError because the array is filled with infinities
print(arr)
