import numpy as np
from scipy.stats.qmc import SobolGaussian

# Generate Sobol' sequences
def generate_sobol_seq(dimensions, num_samples):
    sampler = SobolGaussian(dimensions=dimensions)
    sequence = sampler.random(num_samples)
    return sequence

# Example usage: Generate 1000 2D Sobol' sequences
dimensions = 2
num_samples = 1000
sobol_sequence = generate_sobol_seq(dimensions, num_samples)

print(sobol_sequence)
