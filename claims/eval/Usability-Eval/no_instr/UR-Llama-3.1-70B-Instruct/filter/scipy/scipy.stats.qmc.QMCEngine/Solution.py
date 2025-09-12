import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    """
    A generic Quasi-Monte Carlo sampler class meant for subclassing.
    """
    def __init__(self, dim, seed=42):
        """
        Parameters:
        ----------
        dim : int
            The number of dimensions for the sampler.
        seed : int, optional
            The seed for reproducibility (default is 42).
        """
        self.dim = dim
        self.seed = seed

    def sample(self, n_samples):
        """
        Sample from the Quasi-Monte Carlo sequence.

        Parameters:
        ----------
        n_samples : int
            The number of samples to generate.

        Returns:
        -------
        samples : ndarray
            A 2D array of shape (n_samples, dim) containing the samples.
        """
        sampler = qmc.Halton(d=self.dim, scramble=False, seed=self.seed)
        samples = sampler.random(n=n_samples)
        return samples

    def _transform_samples(self, samples):
        """
        Optional: transform the samples from the unit hypercube to some other space.

        Parameters:
        ----------
        samples : ndarray
            A 2D array of shape (n_samples, dim) containing the samples.

        Returns:
        -------
        transformed_samples : ndarray
            A 2D array of shape (n_samples, dim) containing the transformed samples.
        """
        raise NotImplementedError("Subclass must implement this method")

# Example usage
if __name__ == "__main__":
    sampler = QuasiMonteCarloSampler(dim=3)
    n_samples = 10
    samples = sampler.sample(n_samples)
    print(samples)
