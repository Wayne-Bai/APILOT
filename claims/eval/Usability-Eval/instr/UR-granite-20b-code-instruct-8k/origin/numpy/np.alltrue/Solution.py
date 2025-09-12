import numpy as np

# Please provide the numpy array and the axis you want to test
arr = np.array([[1, 2], [3, 4]])
axis = 0

# Use np.all() to test whether all elements along the given axis evaluate to True
result = np.all(arr, axis=axis)

print(result)
