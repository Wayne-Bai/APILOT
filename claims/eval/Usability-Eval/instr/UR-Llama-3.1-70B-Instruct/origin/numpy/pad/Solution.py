import numpy as np

# Create a numpy array
array = np.array([1, 2, 3, 4, 5])

# Pad the array with 2 elements before and after
padded_array = np.pad(array, 2)

print("Original Array:")
print(array)

print("\nPadded Array:")
print(padded_array)

# Pad the array with different values before and after
padded_array_with_values = np.pad(array, 2, mode='constant', constant_values=0)

print("\nPadded Array with values:")
print(padded_array_with_values)

# Pad the array with specific values before and after
padded_array_with_specific_values = np.pad(array, (2, 3), mode='constant', constant_values=10)

print("\nPadded Array with specific values:")
print(padded_array_with_specific_values)
