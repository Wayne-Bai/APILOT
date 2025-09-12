from scipy.stats import qmc

# Define the number of samples and dimensions
n = 1000
samples = 2

# Create the Latin Hypercube Samples
lhs = qmc.LatinHypercube(d=samples)
samples = lhs.random(n=n)

# Print the first 5 samples
print(samples[:5])
