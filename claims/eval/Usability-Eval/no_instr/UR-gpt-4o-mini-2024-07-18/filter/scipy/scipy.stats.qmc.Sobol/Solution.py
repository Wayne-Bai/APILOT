import numpy as np
from scipy.statlib import qmc

def generate_scrambled_sobol_samples(dimension, n_samples):
    # Create a Sobol sequence instance
    sobol = qmc.Sobol(d=dimension, scramble=True)
    
    # Generate the samples
    samples = sobol.random(n=n_samples)
    
    return samples

# Example usage
dimension = 3  # Number of dimensions
n_samples = 10  # Number of samples
scrambled_sobol_samples = generate_scrambled_sobol_samples(dimension, n_samples)
print(scrambled_sobol_samples)
