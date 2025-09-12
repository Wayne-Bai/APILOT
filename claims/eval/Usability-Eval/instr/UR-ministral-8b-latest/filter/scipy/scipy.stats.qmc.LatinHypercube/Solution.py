import numpy as np
from scipy.stats import uniform

def latin_hypercube_sampling(num_points, num_params):
    sample = []
    a = [uniform.random() * (max - min) + min for min, max in sample_range]
    sample.extend(uniform.ppf(a / max, loc, scale = 1))
    return np.array(sample).T

# Example usage
num_points = 10
num_params = 5
sample_range = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
samples = latin_hypercube_sampling(num_points, num_params)
print(samples)
