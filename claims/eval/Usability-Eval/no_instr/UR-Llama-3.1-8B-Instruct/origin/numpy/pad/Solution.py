import numpy as np

# Define the original array
arr = np.random.randint(0,10,size=(3,3))
print("Original Array:")
print(arr)

# Define the padding mode and the amount of padding
padding_mode      = 'constant'        # constant, edge, linear_ramp, maximum, median, minimum, symmetric, wrap
padding_amount_row = 1                 # number of pixels to add along the row axis
padding_amount_col = 1                 # number of pixels to add along the column axis

# Pad the array
padded_arr = np.pad(arr, 
                    pad_width=((padding_amount_row,padding_amount_col),
                               (padding_amount_row,padding_amount_col)),
                    mode=padding_mode)

print("\nArray after padding:")
print(padded_arr)
