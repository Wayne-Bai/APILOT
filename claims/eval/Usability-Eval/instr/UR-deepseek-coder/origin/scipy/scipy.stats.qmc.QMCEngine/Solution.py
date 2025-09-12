import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    def __init__(self, n_samples, dim):
        self.n_samples = n_samples
        self.dim = dim
        self.engine = qmc.Sobol(d=dim)
        self.sample_points = self.engine.random(n=n_samples)

    def sample(self):
        return self.sample_points

    def resample(self, n_samples=None):
        if n_samples is None:
            n_samples = self.n_samples
        self.sample_points = self.engine.random(n=n_samples)
        return self.sample_points

# Example usage:
# qmc_sampler = QuasiMonteCarloSampler(n_samples=100, dim=2)
# samples = qmc_sampler.sample()
# print(samples)
