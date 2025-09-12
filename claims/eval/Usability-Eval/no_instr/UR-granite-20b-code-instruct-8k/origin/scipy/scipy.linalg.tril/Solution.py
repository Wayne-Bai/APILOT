import numpy as np

def zero_out_above_diagonal(matrix, k):
    """
    Make a copy of a matrix with elements above the kth diagonal zeroed.

    Parameters
    ----------
    matrix : array_like
        The input matrix.
    k : int
        The diagonal above which to zero elements.

    Returns
    -------
    zeros_matrix : ndarray
        A copy of the input matrix with elements above the kth diagonal zeroed.

    Examples
    --------
    >>> matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> zero_out_above_diagonal(matrix, 1)
    array([[0., 2., 3.],
           [0., 0., 6.],
           [0., 0., 0.]])
    """
    zeros_matrix = np.copy(matrix)
    zeros_matrix[np.triu_indices_from(zeros_matrix, k=k+1)] = 0
    return zeros_matrix
