import numpy as np

# Sample array
array = np.array([1, 2, 3, 4, 5])

# Specifying amount of padding for each dimension (symmetric padding in this example)
pad_width = 2  # pads with 2 elements on each side

# Padding the array
padded_array = np.pad(array, pad_width, mode='constant', constant_values=0)

print("Original array:", array)
print("Padded array:", padded_array)
