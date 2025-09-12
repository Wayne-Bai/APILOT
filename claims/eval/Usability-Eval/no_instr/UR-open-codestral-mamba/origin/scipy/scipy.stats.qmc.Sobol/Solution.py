from scipy.stats.qmc import Sobol

# Set the number of dimensions for the Sobol' sequence
dim = 2

# Initialize the Sobol' sequence generator
sobol = Sobol(dim)

# Generate the first n samples
n = 10
samples = sobol.random(n)

# Print the generated samples
print(samples)
