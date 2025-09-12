import numpy as np

# Sample array
arr = np.array([[True, False, True], [False, True, False], [True, True, True]])

# Test if all elements along axis=0 evaluate to True
result_0 = np.all(arr, axis=0)
print("All elements along axis=0 evaluate to True: ", result_0)

# Test if all elements along axis=1 evaluate to True
result_1 = np.all(arr, axis=1)
print("All elements along axis=1 evaluate to True: ", result_1)
