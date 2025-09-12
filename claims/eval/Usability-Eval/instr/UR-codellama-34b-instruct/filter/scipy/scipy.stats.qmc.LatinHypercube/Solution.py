# Import libraries
import numpy as np
from scipy.stats import qmc

# Define parameters for LHS
n_dim = 2     # number of dimensions
lb = [0, 1]   # lower bounds for each dimension
ub = [1, 2]   # upper bounds for each dimension
n_points = 16 # number of points to be generated within each dimension

# Generate LHS samples
lhs = qmc.LatinHypercube(n_dim, lb, ub, n_points)

# Print the generated samples
print(lhs)
