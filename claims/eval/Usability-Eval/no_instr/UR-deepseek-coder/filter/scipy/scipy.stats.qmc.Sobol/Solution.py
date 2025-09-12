import numpy as np
from scipy.stats import qmc

# Initialize the Sobol' sequence generator
engine = qmc.Sobol(d=2, scramble=True)

# Generate 10 Sobol' sequences
sequences = engine.random(n=10)

print(sequences)
