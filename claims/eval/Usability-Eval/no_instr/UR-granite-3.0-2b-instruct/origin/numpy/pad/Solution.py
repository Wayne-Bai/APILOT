import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros on the right side
padded_arr = np.pad(arr, (len(arr), 0), 'constant')

# Print the padded array
print(padded_arr)
