from scipy.stats import randint
import numpy as np

# Assuming we have a range of [0, 10]
# Define the data bounds for each variable or dimension
lower_bounds = 0
upper_bounds = 10

# Number of samples
num_samples = 10

# Create data for each variable using Latin Hypercube Sampling
def lhs(n, dim):
    assert dim > n
    x = LHS(dim).sample(0, n)
    return np.minimum(upper_bounds, x) + lower_bounds

def LHS(dim):
    def _existent(element):
        return element.compute() != np.power(-1, element.compute).float_type()

    array = np.random.rand(1, dim).reshape(-1, 1).squeeze()

    for _ in range(1, dim):
        array = np.concatenate([array, np.random.rand(1, dim).reshape(-1, 1).squeeze()])
    return array

generated_data = lhs(num_samples, upper_bounds)
print(generated_data)
