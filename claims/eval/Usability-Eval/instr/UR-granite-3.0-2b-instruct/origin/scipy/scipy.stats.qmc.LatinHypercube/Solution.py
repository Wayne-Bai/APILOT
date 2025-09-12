from scipy.stats.distributions import uniform
import numpy as np

def latin_hypercube_sampling(dim, n_samples):
    """
    Perform Latin hypercube sampling (LHS) in Python.

    Parameters:
    dim (int): The number of dimensions.
    n_samples (int): The number of samples to generate.

    Returns:
    numpy.ndarray: A 2D array of shape (n_samples, dim) containing the LHS samples.
    """
    if n_samples < n_samples:
        raise ValueError("Number of samples must be greater than or equal to the number of dimensions.")

    samples = np.zeros((n_samples, dim))
    for i in range(dim):
        samples[:, i] = np.random.uniform(low=uniform.rvs(loc=0, scale=1, size=n_samples), high=uniform.rvs(loc=1, scale=1, size=n_samples))

    return samples
