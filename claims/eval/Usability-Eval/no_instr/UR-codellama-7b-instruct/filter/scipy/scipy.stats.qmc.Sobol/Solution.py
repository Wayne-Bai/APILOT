
import scipy.stats as stats

def scrambled_sobol_sequence(n, k):
    """
    Generates a scrambled Sobol' sequence of length n and dimension k using SciPy.

    Args:
        n (int): Length of the sequence.
        k (int): Dimension of the space.

    Returns:
        A tuple of size k, each element being an ndarray of shape (n,). The arrays contain the generated sequence.
    """
    # Generate a standard Sobol' sequence
    sobol_seq = stats.sobol_sequence(n, k)

    # Shuffle the columns of the standard Sobol' sequence
    shuffled_sobol_seq = np.random.permutation(sobol_seq).T

    return shuffled_sobol_seq
