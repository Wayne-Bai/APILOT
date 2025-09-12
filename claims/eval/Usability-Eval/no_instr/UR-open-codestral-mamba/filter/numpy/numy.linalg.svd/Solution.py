import numpy as np

# Let's create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

U, S, V = np.linalg.svd(array)

print("U: \n", U)
print("S: \n", S)
print("V: \n", V)
