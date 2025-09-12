import scipy.sparse as sp

def is_sparse(matrix):
    if sp.issparse(matrix):
        return True
    else:
        return False

# Test the function
matrix = sp.csr_matrix([[0, 0, 0], [0, 0, 1], [0, 2, 0]])

result = is_sparse(matrix)
result
