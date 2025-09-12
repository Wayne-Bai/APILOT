import numpy as np
from scipy.stats import norm

class QuasiMonteCarloSampler:
    def __init__(self, data, mu=0, sigma=1):
        self.data = data
        self.mu = mu
        self.sigma = sigma

    def sample(self, n_samples):
        return np.random.normal(self.mu, self.sigma, size=n_samples) + self.data
