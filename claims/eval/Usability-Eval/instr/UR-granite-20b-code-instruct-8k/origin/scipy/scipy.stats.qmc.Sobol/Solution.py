from scipy.stats import qmc

# Set the number of dimensions and the number of samples
dim = 2
n = 1000

# Generate a scrambled Sobol' sequence
rng = qmc.Sobol(d=dim, scramble=True)
samples = rng.random(n)
