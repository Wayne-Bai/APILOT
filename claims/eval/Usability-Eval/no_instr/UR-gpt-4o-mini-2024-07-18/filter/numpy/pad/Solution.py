import numpy as np

# Function to pad an array
def pad_array(arr, pad_width, mode='constant', constant_values=0):
    if mode == 'constant':
        return np.pad(arr, pad_width, mode=mode, constant_values=constant_values)
    else:
        raise ValueError("Unsupported mode. Only 'constant' mode is implemented.")

# Example usage
array = np.array([[1, 2], [3, 4]])
padded_array = pad_array(array, pad_width=1, mode='constant', constant_values=0)
print(padded_array)
