import numpy as np
from scipy.sparse import csr_matrix

def generate_design_matrix(rows, cols, dtype=np.float64):
    # Create a random design matrix
    data = np.random.rand(rows, cols, dtype=dtype)

    # Indices
    row_indices = np.array([i for i in range(rows*cols) for _ in range(cols)])
    col_indices = np.repeat(np.arange(cols), rows)
    nnz = np.sum(data != 0)

    # Coordinates and Data array
    row_data = np.empty((nnz,), dtype=dtype)
    col_data = np.empty((nnz,), dtype=None)

    row_data[0:nnz - 1] = data[0:nnz - 1, 0]
    row_data[nnz - 1] = 0

    col_data[0:nnz - 1] = data[0:nnz - 1, 1]
    col_data[nnz - 1] = 0

    # Create and return the CSR matrix
    csr_matrix = csr_matrix((row_data, (row_indices[:nnz], col_indices[:nnz])), shape=(rows, cols))
    return csr_matrix

# Example usage
rows = 1000
cols = 500
sparse_matrix = generate_design_matrix(rows, cols)
print(sparse_matrix)
