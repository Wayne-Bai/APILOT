
import scipy.stats as stats

# Define the number of dimensions for the Sobol sequence
ndim = 2

# Generate the Sobol sequence
sobol_seq = stats.qmc(ndim, n=10000)

print(sobol_seq[:10])
