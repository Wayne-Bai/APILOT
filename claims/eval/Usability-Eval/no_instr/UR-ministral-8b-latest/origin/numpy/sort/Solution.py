import numpy as np

def sorted_array(input_array):
    return np.sort(input_array)

# Example usage
input_array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
sorted_array_result = sorted_array(input_array)
print(sorted_array_result)
