import numpy as np

def find_max_indices(arr, axis=-1):
    if axis == 0:
        return np.unravel_index(np.argmax(arr, axis=axis), arr.shape)
    elif axis == 1:
        max_values = np.argmax(arr, axis=axis)
        final_indices = []
        for row in max_values:
            final_indices.append(row)
        return final_indices

# Example usage
array = np.array([[3, 8, 1], [7, 2, 5]])
result = find_max_indices(array, axis=-1)
print(result)
