import numpy as np
from scipy.stats import qmc

class GenericQuasiMonteCarloSampler:
    def __init__(self, dim, n):
        self.dim = dim  # Dimensionality of the problem
        self.n = n  # Number of samples

    def sample(self):
        raise NotImplementedError("Subclasses must implement the sampling method.")

class SobolQuasiMonteCarloSampler(GenericQuasiMonteCarloSampler):
    def __init__(self, dim, n):
        super().__init__(dim, n)
        self.sampler = qmc.Sobol(d=self.dim, scramble=True)  # Initialize Sobol sampler with scrambling

    def sample(self):
        return self.sampler.random(n=self.n)  # Return the samples
