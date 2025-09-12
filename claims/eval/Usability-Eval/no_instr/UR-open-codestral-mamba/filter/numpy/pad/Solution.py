import numpy as np

# Define the initial array
arr = np.array([[1, 2], [3, 4]])

# Print the initial array
print("Initial array:")
print(arr)

# Pad the array with a constant value (e.g., 0)
# np.pad takes the following arguments:
# 1. The input array
# 2. The number of values to pad for each axis in the beginning and end of each axis
# 3. The type of padding to apply (constant in our case)
# 4. The constant value to be used for padding
padded_arr = np.pad(arr, ((1, 1), (1, 1)), 'constant', constant_values=0)

# Print the padded array
print("Padded array:")
print(padded_arr)
