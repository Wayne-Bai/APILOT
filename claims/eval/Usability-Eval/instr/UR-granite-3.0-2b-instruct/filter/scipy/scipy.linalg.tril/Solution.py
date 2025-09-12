from scipy.sparse import csr_matrix

def zero_above_kth_diagonal(matrix, k):
    # Convert the input matrix to a sparse matrix
    matrix = csr_matrix(matrix)

    # Create a copy of the sparse matrix
    copy = matrix.copy()

    # Set the elements above the kth diagonal to zero
    copy[copy.row > k - 1, copy.col > k - 1] = 0

    return copy
