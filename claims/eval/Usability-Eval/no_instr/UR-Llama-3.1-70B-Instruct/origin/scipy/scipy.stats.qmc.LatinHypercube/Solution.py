import numpy as np
from scipy.stats import qmc

def latin_hypercube_sampling(dimensions, samples, seed=None):
    """
    Generates Latin Hypercube Samples.

    Parameters:
    dimensions (int): Number of dimensions for the sample space.
    samples (int): Number of samples to generate.
    seed (int): Seed for the random number generator.

    Returns:
    np.ndarray: A 2D array with shape (samples, dimensions) containing the LHS.
    """
    # Initialize the Latin Hypercube sampler
    sampler = qmc.LatinHypercube(d=dimensions, seed=seed)

    # Generate the sample
    sample = sampler.random(n=samples)

    return sample

# Example usage
dimensions = 3  # Specify the number of dimensions
samples = 100  # Specify the number of samples

# Generate Latin Hypercube Samples
lhs_samples = latin_hypercube_sampling(dimensions, samples)

print(lhs_samples)
