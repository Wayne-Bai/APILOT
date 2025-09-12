import numpy as np

def find_indices_of_max(arr, axis):
    return np.argmax(arr, axis=axis)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
axis = 1

print(find_indices_of_max(arr, axis))