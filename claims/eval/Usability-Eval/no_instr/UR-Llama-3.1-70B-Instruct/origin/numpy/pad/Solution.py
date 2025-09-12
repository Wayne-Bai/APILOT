import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Pad the array with zeros on both sides
padded_arr = np.pad(arr, (2, 2), mode='constant', constant_values=0)

print("Original Array: ", arr)
print("Padded Array: ", padded_arr)

# Pad the array with zeros on the left side
padded_arr_left = np.pad(arr, (2, 0), mode='constant', constant_values=0)

print("Padded Array (Left): ", padded_arr_left)

# Pad the array with zeros on the right side
padded_arr_right = np.pad(arr, (0, 2), mode='constant', constant_values=0)

print("Padded Array (Right): ", padded_arr_right)

# Pad the array with values from the edge
padded_arr_edge = np.pad(arr, (2, 2), mode='edge')

print("Padded Array (Edge): ", padded_arr_edge)

# Pad the array with linear extrapolation
padded_arr_linear = np.pad(arr, (2, 2), mode='linear_ramp', end_values=(0, 0))

print("Padded Array (Linear): ", padded_arr_linear)
