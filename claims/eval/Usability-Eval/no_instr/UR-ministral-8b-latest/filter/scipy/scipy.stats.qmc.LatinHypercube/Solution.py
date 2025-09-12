import numpy as np
from scipy.stats import qmc

def latin_hypercube_sampling(dimensions, samples):
    sample = qmc.LatinHypercube(dim=dimensions)(samples)
    return sample

# Example usage
dimensions = 3  # number of dimensions
samples = 10   # number of samples
samples = latin_hypercube_sampling(dimensions, samples)
print(samples)
