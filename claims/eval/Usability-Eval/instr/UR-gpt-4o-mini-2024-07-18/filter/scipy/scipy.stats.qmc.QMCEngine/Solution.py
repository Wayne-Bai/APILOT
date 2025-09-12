import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    def __init__(self, dimensions, n_samples):
        self.dimensions = dimensions
        self.n_samples = n_samples
        self.sampler = self.create_sampler()
        self.samples = self.generate_samples()

    def create_sampler(self):
        """Create a QMC sampler specific to the subclass."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def generate_samples(self):
        """Generate required number of samples using the QMC sampler."""
        return self.sampler.random(self.n_samples)

class SobolSampler(QuasiMonteCarloSampler):
    def create_sampler(self):
        """Create a Sobol sequence sampler."""
        return qmc.Sobol(d=self.dimensions)

class HaltonSampler(QuasiMonteCarloSampler):
    def create_sampler(self):
        """Create a Halton sequence sampler."""
        return qmc.Halton(d=self.dimensions)

# Example usage
if __name__ == "__main__":
    dimensions = 2
    n_samples = 1000

    sobol_sampler = SobolSampler(dimensions, n_samples)
    halton_sampler = HaltonSampler(dimensions, n_samples)

    print("Sobol Samples:\n", sobol_sampler.samples)
    print("Halton Samples:\n", halton_sampler.samples)
