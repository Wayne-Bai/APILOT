import numpy as np
from scipy.stats import uniform

class QuasiMonteCarloSampler:
    def __init__(self, dimension, dimensionality=1, seed=None):
        self.dimension = dimension
        self.dimensionality = dimensionality
        self.seed = seed
        self.np_random = np.random.RandomState(seed)

    def sample(self, n_samples):
        if self.dimensionality == 1:
            return self._sample_1d(n_samples)
        else:
            return self._sample_nd(n_samples)

    def _sample_1d(self, n_samples):
        low, high = 0, 1
        return self.np_random.uniform(low, high, size=(n_samples, self.dimension))

    def _sample_nd(self, n_samples):
        low, high = 0, 1
        return self.np_random.uniform(low, high, size=(n_samples, self.dimensionality))
