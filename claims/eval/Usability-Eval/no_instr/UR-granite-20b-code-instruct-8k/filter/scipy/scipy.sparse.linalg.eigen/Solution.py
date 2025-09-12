import scipy as sp
A = sp.array([[1,2,3],[4,5,6],[7,8,9]])
evals, evecs = sp.linalg.eig(A)
print("Eigenvalues:")
print(evals)
print("Eigenvectors:")
print(evecs)
