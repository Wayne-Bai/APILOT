import numpy as np
from scipy.stats import norm

class QuasiMonteCarloSampler:
    def __init__(self, dim, sampler_type):
        self.dim = dim
        self.sampler_type = sampler_type
        self.samples = None

    def generate_samples(self, n):
        if self.sampler_type == 'Sobol':
            # Generate Sobol sequences
            self.samples = np.random.sobol(n, self.dim)
        elif self.sampler_type == 'Halton':
            # Generate Halton sequences
            self.samples = np.random.halton(n, self.dim)
        else:
            raise ValueError("Invalid sampler type")
        return self.samples
