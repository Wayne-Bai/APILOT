# Importing the required library numpy
import numpy as np

# Creating a 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Performing singular value decomposition on the array
U, S, V = np.linalg.svd(arr)

print(f"U: \n{U}")
print(f"S: \n{S}")
print(f"V: \n{V}")
