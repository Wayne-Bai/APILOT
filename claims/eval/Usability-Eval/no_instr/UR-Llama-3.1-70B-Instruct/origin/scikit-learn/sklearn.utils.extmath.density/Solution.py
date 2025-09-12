# Import necessary libraries
from sklearn.utils import sparse
import numpy as np

# Function to compute density of a sparse vector
def compute_density(X):
    """
    Compute the density of a sparse vector.

    Density is defined as the ratio of non-zero elements to the total number of elements.

    Parameters
    ----------
    X : sparse matrix or array
        Input sparse data.

    Returns
    -------
    density : float
        Density of the input sparse data.
    """
    # Check if the input is a sparse matrix
    if sparse.issparse(X):
        # Get the number of non-zero elements and the total number of elements
        num_non_zero = X.count_nonzero()
        num_total = X.shape[0] * X.shape[1]
        # Compute the density
        density = num_non_zero / num_total
    else:
        # Check if the input is a numpy array
        if isinstance(X, np.ndarray):
            # Get the number of non-zero elements and the total number of elements
            num_non_zero = np.count_nonzero(X)
            num_total = X.size
            # Compute the density
            density = num_non_zero / num_total
        else:
            raise ValueError("Input must be a sparse matrix or a numpy array.")

    return density

# Example usage:
if __name__ == "__main__":
    # Create a sparse vector
    sparse_vector = sparse.csr_matrix(np.array([1, 0, 2, 0, 3]))
    print("Sparse Vector:")
    print(sparse_vector.toarray())

    # Compute the density
    density = compute_density(sparse_vector)
    print("Density:", density)

    # Create a non-sparse vector
    non_sparse_vector = np.array([1, 2, 3, 4, 5])
    print("Non-Sparse Vector:")
    print(non_sparse_vector)

    # Compute the density
    density = compute_density(non_sparse_vector)
    print("Density:", density)
