import numpy as np
from scipy.sparse import csc_matrix

def create_matrix(N, M, k):
    # Create a sparse matrix with ones at and below the kth diagonal
    A = csc_matrix(np.ones((N, M), dtype=int))
    A = A[:N, :N-k] + A[:N, N-k:N]
    return A
