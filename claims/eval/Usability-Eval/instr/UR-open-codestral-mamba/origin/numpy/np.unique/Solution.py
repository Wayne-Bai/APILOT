import numpy as np

def get_unique_elements(arr):
    return np.sort(np.unique(arr))

# testing the function
arr = np.array([3, 1, 2, 2, 4, 5, 5, 5])
print(get_unique_elements(arr))
