from scipy import sparse
import numpy as np

def csr_format(my_matrix):
    csr_matrix = sparse.csr_matrix(np.array(my_matrix))
    return csr_matrix

# Example usage:
my_design_matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
csr_matrix = csr_format(my_design_matrix)
print(csr_matrix)
