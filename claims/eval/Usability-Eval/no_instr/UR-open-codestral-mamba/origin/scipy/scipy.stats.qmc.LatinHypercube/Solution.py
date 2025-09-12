import numpy as np
from scipy.stats import qmc

# Define the function for Latin Hypercube Sampling
def lhs(n_samples, n_features):
    sampler = qmc.LatinHypercube(d=n_features)
    sample = sampler.random(n=n_samples)
    return sample

# Generate LHS sample for 10 samples and 3 features
sample = lhs(10, 3)
print(sample)
