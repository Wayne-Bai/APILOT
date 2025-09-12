import scipy.sparse as sp

# Example to create a design matrix as a CSR (Compressed Sparse Row) sparse array.
# Here we create a 3x2 matrix, but you can specify any size and elements.

data = [1, 2, 3]
row_indices = [0, 1, 2]
col_indices = [0, 0, 1]

design_matrix = sp.csr_matrix((data, (row_indices, col_indices)), shape=(3, 2))

print(design_matrix)
