import scipy.stats as stats
from abc import ABC, abstractmethod

class QuasiMonteCarloSampler(ABC):

    def __init__(self, dimension):
        self.dimension = dimension

    @abstractmethod
    def sample(self, n):
        pass
