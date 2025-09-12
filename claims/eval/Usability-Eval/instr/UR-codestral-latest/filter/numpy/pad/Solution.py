import numpy as np

# Let's assume 'array' is the given array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Using np.pad to add padding to the array
# Pad with 0 on all sides, so it's '2' times larger
padded_array = np.pad(array, pad_width=2, mode='constant')

print("Padded Array:")
print(padded_array)
