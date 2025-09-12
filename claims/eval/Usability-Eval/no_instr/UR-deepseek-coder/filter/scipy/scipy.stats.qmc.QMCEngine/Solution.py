import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    def __init__(self, n_samples, d):
        self.n_samples = n_samples
        self.d = d
        self.engine = qmc.Sobol(d=d)
        self.sample_points = self.engine.random(n=n_samples)

    def sample(self):
        return self.sample_points

    def resample(self, n_samples):
        self.n_samples = n_samples
        self.sample_points = self.engine.random(n=n_samples)
        return self.sample_points

# Example usage:
# sampler = QuasiMonteCarloSampler(n_samples=100, d=2)
# samples = sampler.sample()
# print(samples)
