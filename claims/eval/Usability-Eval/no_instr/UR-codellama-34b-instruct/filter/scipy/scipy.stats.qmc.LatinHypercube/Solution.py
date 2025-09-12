
import numpy as np
from scipy.stats import qmc

# Define the number of samples and dimensions
n_samples = 100
n_dimensions = 5

# Generate random data using the LHS algorithm
lhs_data = qmc.LatinHypercube(n_samples, n_dimensions).generate()

print("LHS samples:")
print(lhs_data)
