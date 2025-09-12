import numpy as np
from scipy.sparse import csr_matrix

def sparse_vector_density(vector):
    """
    Compute the density of a sparse vector.

    Parameters:
    - vector: Sparse vector, e.g., a CSR matrix

    Returns:
    - density: Scalar value representing the density of the sparse vector
    """
    if not isinstance(vector, csr_matrix):
        raise ValueError('Input must be a sparse matrix (CSR format).')

    count_nonzero = vector.nnz
    norm_vector = float(np.count_nonzero(vector))
    density = count_nonzero / norm_vector
    return density
