import numpy as np

def singular_value_decomposition(matrix):
    """
    Perform Singular Value Decomposition on a given matrix.

    Parameters:
    matrix (numpy.ndarray): Input matrix for SVD.

    Returns:
    U (numpy.ndarray), s (numpy.ndarray), Vh (numpy.ndarray): 
    The decomposed matrices.
    """

    # Ensure the input matrix is a numpy array
    matrix = np.array(matrix)

    # Get the shape of the input matrix
    m, n = matrix.shape

    # If m > n, perform SVD on matrix transpose to reduce computation
    if m > n:
        U, s, Vh = np.linalg.svd(matrix.T, full_matrices=False)
        # Swap U and Vh
        U, Vh = Vh.T, U.T
    else:
        U, s, Vh = np.linalg.svd(matrix, full_matrices=False)

    return U, s, Vh


# Example usage:
if __name__ == "__main__":
    # Define a matrix
    matrix = np.array([[1, 0, 0, 0, 2],
                       [0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 2, 0, 0, 0]])

    U, s, Vh = singular_value_decomposition(matrix)

    print("Matrix U:")
    print(U)
    print("\nSingular values:")
    print(s)
    print("\nMatrix Vh:")
    print(Vh)

    # Verify the decomposition by reconstructing the original matrix
    reconstructed_matrix = U @ np.diag(s) @ Vh
    print("\nReconstructed Matrix:")
    print(reconstructed_matrix)
