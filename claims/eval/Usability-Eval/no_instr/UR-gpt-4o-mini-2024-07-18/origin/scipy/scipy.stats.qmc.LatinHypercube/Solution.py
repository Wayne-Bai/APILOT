import numpy as np
from scipy.stats import qmc

def latin_hypercube_sampling(samples: int, dimensions: int):
    # Create a Latin Hypercube Sampler
    sampler = qmc.LatinHypercube(d=dimensions)
    
    # Generate samples
    sampled_points = sampler.random(n=samples)
    
    return sampled_points

# Example usage
if __name__ == "__main__":
    num_samples = 10
    num_dimensions = 3
    samples = latin_hypercube_sampling(num_samples, num_dimensions)
    print(samples)
