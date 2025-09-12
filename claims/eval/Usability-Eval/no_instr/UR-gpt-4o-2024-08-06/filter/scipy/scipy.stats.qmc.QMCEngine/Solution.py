import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    def __init__(self, dimension, num_samples):
        self.dimension = dimension
        self.num_samples = num_samples
        self.sampler = None

    def generate_samples(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

class SobolSampler(QuasiMonteCarloSampler):
    def __init__(self, dimension, num_samples):
        super().__init__(dimension, num_samples)
        self.sampler = qmc.Sobol(d=self.dimension, scramble=False)

    def generate_samples(self):
        return self.sampler.random(n=self.num_samples)

class HaltonSampler(QuasiMonteCarloSampler):
    def __init__(self, dimension, num_samples):
        super().__init__(dimension, num_samples)
        self.sampler = qmc.Halton(d=self.dimension, scramble=False)

    def generate_samples(self):
        return self.sampler.random(n=self.num_samples)

# Example usage:
# sobol_sampler = SobolSampler(dimension=2, num_samples=10)
# samples = sobol_sampler.generate_samples()
# print("Sobol Samples:\n", samples)

# halton_sampler = HaltonSampler(dimension=2, num_samples=10)
# samples = halton_sampler.generate_samples()
# print("Halton Samples:\n", samples)
