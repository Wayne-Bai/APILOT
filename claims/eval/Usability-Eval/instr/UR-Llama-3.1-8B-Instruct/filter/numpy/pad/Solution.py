import numpy as np

# Define an array
array = np.array([1, 2, 3, 4, 5])

# Print the original array
print("Original array:")
print(array)

# Pad the array with 1 on the left
padded_array_left = np.pad(array, (1, 0), mode='constant', constant_values=1)
print("\nArray padded on the left with 1:")
print(padded_array_left)

# Pad the array with 1 on the right
padded_array_right = np.pad(array, (0, 1), mode='constant', constant_values=1)
print("\nArray padded on the right with 1:")
print(padded_array_right)

# Pad the array with 0 on both sides
padded_array_both = np.pad(array, (1, 1), mode='constant', constant_values=0)
print("\nArray padded on both sides with 0:")
print(padded_array_both)

# Pad the array with a pattern on the left
pattern = np.array([1, 0])
padded_array_pattern_left = np.pad(array, (1, 0), mode='constant', constant_values=pattern[0])
print("\nArray padded on the left with pattern [1, 0]:")
print(padded_array_pattern_left)

# Pad the array with a pattern on the right
padded_array_pattern_right = np.pad(array, (0, 1), mode='constant', constant_values=pattern[1])
print("\nArray padded on the right with pattern [1, 0]:")
print(padded_array_pattern_right)

# Pad the array with a pattern on both sides
padded_array_pattern_both = np.pad(array, (1, 1), mode='constant', constant_values=pattern)
print("\nArray padded on both sides with pattern [1, 0]:")
print(padded_array_pattern_both)
