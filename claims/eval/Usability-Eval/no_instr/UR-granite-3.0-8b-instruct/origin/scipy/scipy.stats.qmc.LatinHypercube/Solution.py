import numpy as np
from scipy.stats import norm
from scipy.spatial.distance import euclidean

def lhs_sampling(n, p, lower_bound, upper_bound):
    # Generate random numbers between 0 and 1
    random_numbers = np.random.rand(n, p)

    # Scale and shift the random numbers to the desired range
    lhs_samples = lower_bound + (upper_bound - lower_bound) * random_numbers

    return lhs_samples

# Example usage:
n = 100  # number of samples
p = 3  # number of variables
lower_bound = np.array([0, 0, 0])
upper_bound = np.array([1, 1, 1])

lhs_samples = lhs_sampling(n, p, lower_bound, upper_bound)
print(lhs_samples)
