import numpy as np

# For padding, let's use np.pad function's constant padding
# Here is an example of padding an array

# Defining the original array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Padding the array with 0 using a constant padding
padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)

print(padded_arr)
