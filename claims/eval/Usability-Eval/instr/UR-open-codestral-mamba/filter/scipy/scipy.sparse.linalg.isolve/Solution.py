# Import required libraries
from scipy import sparse
from scipy.sparse.linalg import spsolve
import numpy as np

# Define a 5x5 sparse matrix for A
A = sparse.diags([1, 2, 3, 4, 5], [0], shape=(5, 5)).toarray()

# Define a 5x1 dense matrix for b
b = np.array([6, 7, 8, 9, 10])

# Solve for x
x = spsolve(A, b)

print("The solution for x is: ")
print(x)
