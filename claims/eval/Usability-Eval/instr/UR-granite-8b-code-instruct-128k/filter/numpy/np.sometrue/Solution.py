import numpy as np

# Define the array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Test whether any array element along a given axis evaluates to True.
result = np.any(array > 3, axis=1)

print(result)  # Output: [False False  True]