import scipy.stats as stats
import numpy as np

class QMCSampler:
    def __init__(self, dim):
        self.dim = dim
        self.sampler = stats.qmc.Sobol(dim)

    def sample(self, n):
        return self.sampler.random(n)
