import numpy as np
from scipy.stats import qmc

def lhs(n_samples, n_features):
    """
    Latin Hypercube Sampling

    Parameters:
    n_samples (int): number of samples to generate
    n_features (int): number of dimensions (features)

    Returns:
    numpy.ndarray: the samples in a numpy array
    """

    # Generate random samples within the interval [0, 1)
    rng = np.random.default_rng()
    samples = rng.random((n_samples, n_features))

    # Scale and shift the samples to [0, 1]
    lhs_samples = qmc.scale(samples, 0, 1)

    return lhs_samples

# Example usage
samples = lhs(100, 5)
print(samples)
