import scipy.stats as stats

def generate_scrambled_sobol(dim, n_samples, seed=None):
    """
    Generate scrambled Sobol' sequences.

    Parameters:
    -----------
    dim : int
        The dimension of the sequence.
    n_samples : int
        The number of samples to generate.
    seed : int, optional
        The seed for the random number generator. Default is None.

    Returns:
    --------
    samples : array-like
        The generated samples.
    """
    sampler = stats.qmc.Sobol(dim, seed=seed)
    samples = sampler.generate(n_samples)
    samples = stats.qmc.scale(samples, 0, 1)

    return samples
