
import scipy.sparse as sp

# Define the sparse matrix
A = sp.csr_matrix([[1,2,0],[3,4,5],[6,7,8]])

# Check if x is a sparse matrix type
print(sp.issparse(x))
