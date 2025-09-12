import numpy as np
from scipy.stats import qmc
import matplotlib.pyplot as plt

# Define the number of samples and dimensions
num_samples = 100
num_dimensions = 2

# Perform Latin Hypercube Sampling (LHS)
lhs_sampler = qmc.LatinHypercube(d=num_dimensions, seed=0)
lhs_samples = lhs_sampler.random(n=num_samples)

# Scale the samples to a specified range
lower_bound = [0, 0]
upper_bound = [10, 10]
scaled_samples = qmc.scale(lhs_samples, lower_bound, upper_bound)

# Print the scaled samples
print(scaled_samples)

# Visualize the samples (optional)
plt.figure(figsize=(8, 8))
plt.scatter(scaled_samples[:, 0], scaled_samples[:, 1])
plt.xlim(lower_bound[0], upper_bound[0])
plt.ylim(lower_bound[1], upper_bound[1])
plt.title("Latin Hypercube Sampling")
plt.show()
