import numpy as np
from scipy.stats import qmc

def generate_sobol_sequence(n_samples, dimensions, scramble=True):
    engine = qmc.Sobol(d=dimensions, scramble=scramble)
    sample = engine.random(n=n_samples)
    return sample

# Example usage:
# Generate 10 samples in 2 dimensions with scrambling
samples = generate_sobol_sequence(10, 2)
print(samples)
