import numpy as np
from scipy.stats import qmc

# Define dimensions and number of samples
dimensions = 2
samples = 1000

# Create a Sobol' sequence
sobol_seq = qmc.Sobol(d=dimensions, scramble=False)

# Generate samples
sample = sobol_seq.random(n=samples)

# Display the first 5 samples
print(sample[:5])
