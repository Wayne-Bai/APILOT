import scipy.sparse as sp
import scipy.linalg as la
import numpy as np

# Example sparse matrix (you can change it to your needs)
A = sp.csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 20, 30])

# Solve the system Ax = b
x = la.spsolve(A, b, use_lapack=True)
print("Solution:", x)
