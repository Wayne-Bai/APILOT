
import numpy as np

class QuasiMonteCarloSampler:
    def __init__(self, dimension):
        self.dimension = dimension

    def generate_samples(self, num_samples):
        samples = np.random.rand(num_samples, self.dimension)
        return samples

# Example usage
sampler = QuasiMonteCarloSampler(dimension=2)
samples = sampler.generate_samples(num_samples=10)
print(samples)
