import scipy.stats as stats

# Define the bounds of the range
a = 0.0
b = 1.0

# Perform Latin hypercube sampling
lhs_array = stats.lhs(a, b, n=100)

# Print the generated samples
print(lhs_array)
