import numpy as np
from scipy.stats import uniform

class QMCSampler:
    def __init__(self, dimension, seed=None):
        self.dimension = dimension
        self.seed = seed
        self.np.random.seed(self.seed)

    def generate(self, n):
        points = self.np.random.uniform(low=0, high=1, size=(n, self.dimension))
        return points

class LatinHypercubeSampler(QMCSampler):
    def __init__(self, dimension, seed=None):
        super().__init__(dimension, seed)

    def generate(self, n):
        points = super().generate(n)
        for i in range(self.dimension):
            points[:, i] = np.sort(points[:, i])
        return points

class SobolSampler(QMCSampler):
    def __init__(self, dimension, seed=None):
        super().__init__(dimension, seed)

    def generate(self, n):
        points = super().generate(n)
        return self.sobol_generate(points)

    def sobol_generate(self, points):
        for i in range(self.dimension):
            points[:, i] = np.random.randn(n) * np.sqrt(2) + np.cos(2 * np.pi * np.arange(n) * (1 + np.arange(self.dimension) / (self.dimension - 1)))
