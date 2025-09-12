from scipy.stats import qmc

# Define the number of samples and dimensions
n = 1000
d = 3

# Create the LHS sampler
lhs = qmc. LatinHypercube(d)

# Generate the samples
samples = lhs.random(n)
