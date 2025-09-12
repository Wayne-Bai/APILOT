import numpy as np
from scipy.stats import qmc

# Define the distribution(s) for the sample
dist1 = qmc.DGauss(mean=0.5, stddev=0.25)
dist2 = qmc.DUniform()

# Set the number of samples to generate
n_samples = 1000

# Generate the samples using Latin Hypercube Sampling
samples = np.array([qmc(n_samples, dists=[dist1, dist2]) for _ in range(n_samples)])

# Print the generated samples
print(samples)
