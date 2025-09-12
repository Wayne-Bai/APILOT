from scipy.sparse import csr_matrix

def zero_below_kth_diagonal(matrix, k):
    # Convert the matrix to a sparse matrix
    matrix = csr_matrix(matrix)

    # Create a new matrix with the same shape as the original
    new_matrix = csr_matrix(matrix.shape)

    # Iterate over the rows and columns of the original matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the element is below the kth diagonal, set it to zero in the new matrix
            if i + j < k:
                new_matrix[i, j] = 0

    return new_matrix
