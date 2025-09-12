
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

padded_arr = np.pad(arr, ((1, 1), (2, 2)), mode='constant', constant_values=0)
print(padded_arr)
