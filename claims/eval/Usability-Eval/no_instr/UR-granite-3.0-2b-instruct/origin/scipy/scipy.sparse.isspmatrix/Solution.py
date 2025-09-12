import scipy as sp

# Assuming 'x' is a sparse matrix
x = sp.sparse.csr_matrix([[0, 1, 0], [2, 0, 3], [0, 0, 0]])

# Check if 'x' is a sparse matrix
if isinstance(x, sp.sparse.csr_matrix):
    print("Yes, 'x' is a sparse matrix.")
else:
    print("No, 'x' is not a sparse matrix.")
