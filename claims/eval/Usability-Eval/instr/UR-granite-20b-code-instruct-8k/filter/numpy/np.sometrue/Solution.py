import numpy as np

# create a numpy array
arr = np.array([[1, 2], [3, 4]])

# check if any element along the first axis evaluates to True
result = np.any(arr, axis=0)

print(result)
