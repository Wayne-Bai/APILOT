import numpy as np
from scipy.stats import qmc

def generate_sobol_sequence(dimensions, n_samples):
    samplers = qmc.Sobol(d=dimensions, scramble=True)
    samples = samplers.random(n=n_samples)
    return samples

# Example usage
dimensions = 2  # Number of dimensions
n_samples = 10  # Number of samples
sobol_samples = generate_sobol_sequence(dimensions, n_samples)
print(sobol_samples)
