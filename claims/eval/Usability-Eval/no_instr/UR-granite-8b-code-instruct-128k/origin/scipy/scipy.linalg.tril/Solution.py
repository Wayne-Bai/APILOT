import scipy as sp

def zero_above_diagonal(A, k):
    """
    Returns a copy of matrix A with elements above the kth diagonal zeroed.

    Args:
    A (ndarray): Input matrix.
    k (int): Index of the diagonal above which elements are set to zero.

    Returns:
    ndarray: Copy of matrix A with elements above the kth diagonal zeroed.
    """
    A_copy = sp.copy(A)
    A_copy[sp.triu_indices_from(A_copy, k+1)] = 0
    return A_copy
