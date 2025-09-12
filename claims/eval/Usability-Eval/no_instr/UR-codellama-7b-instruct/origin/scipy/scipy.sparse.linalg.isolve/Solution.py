import scipy.sparse as sp
A = sp.eye(5)
b = sp.ones((5, 1))
x = sp.spsolve(A, b)
print(x)
