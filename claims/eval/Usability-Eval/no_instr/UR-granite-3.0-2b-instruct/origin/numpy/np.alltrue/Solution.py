import numpy as np

# Create a 2D numpy array
arr = np.array([[True, False, True],
                [False, True, False],
                [True, True, True]])

# Test if all elements along axis=0 (rows) evaluate to True
print("All elements in rows evaluate to True: ", np.all(arr, axis=0))

# Test if all elements along axis=1 (columns) evaluate to True
print("All elements in columns evaluate to True: ", np.all(arr, axis=1))
