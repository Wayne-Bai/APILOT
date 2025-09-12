from scipy.stats import qmc
# Define the number of samples and dimensions
n_samples = 1000
n_dimensions = 3
# Generate the LHS samples
lhs = qmc. LatinHypercube(d=n_dimensions).random(n_samples)
# Print the LHS samples
print(lhs)
