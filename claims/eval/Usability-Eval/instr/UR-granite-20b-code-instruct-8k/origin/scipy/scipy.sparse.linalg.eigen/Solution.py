import scipy as sp

A = sp.array([[1, 2], [3, 4]])
evals, evecs = sp.linalg.eig(A)
print(f"Eigenvalues: {evals}")
print(f"Eigenvectors: {evecs}")