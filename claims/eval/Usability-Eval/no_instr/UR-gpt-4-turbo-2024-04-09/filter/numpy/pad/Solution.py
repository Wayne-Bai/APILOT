import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4])

# Padding the array
padded_array = np.pad(original_array, pad_width=1, mode='constant', constant_values=0)

print("Original array:", original_array)
print("Padded array:", padded_array)
