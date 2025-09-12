
import numpy as np
from scipy.special import comb

def sobol_seq(n, k):
    """
    Generate a Sobol' sequence of length n and dimension k.

    Parameters:
    -----------
    n : int
        Length of the sequence.
    k : int
        Dimension of the sequence.

    Returns:
    --------
    out : ndarray, shape (n, k)
        The Sobol' sequence of length n and dimension k.
    """
    # Initialize the sequence with the first vector
    seq = np.zeros((n, k))
    seq[0] = np.random.rand(k)

    # Compute the remaining vectors using the recurrence relation
    for i in range(1, n):
        seq[i] = comb(seq[i-1], 2) % 2

    return seq
