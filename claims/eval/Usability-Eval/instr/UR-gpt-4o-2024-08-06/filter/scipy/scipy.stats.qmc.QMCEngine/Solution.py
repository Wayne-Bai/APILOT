import numpy as np
from scipy.stats import qmc

class QuasiMonteCarloSampler:
    def __init__(self, dimension, engine='halton'):
        self.dimension = dimension
        self.engine_name = engine.lower()
        self.engine = None

        if self.engine_name == 'halton':
            self.engine = qmc.Halton(d=self.dimension, scramble=True)
        elif self.engine_name == 'sobol':
            self.engine = qmc.Sobol(d=self.dimension, scramble=True)
        elif self.engine_name == 'latin_hypercube':
            self.engine = qmc.LatinHypercube(d=self.dimension)
        else:
            raise ValueError("Unsupported engine type. Supported engines: 'halton', 'sobol', 'latin_hypercube'.")

    def reset(self):
        """Resets the random number generator to start the sequence over."""
        self.engine = self.__create_engine()

    def __create_engine(self):
        if self.engine_name == 'halton':
            return qmc.Halton(d=self.dimension, scramble=True)
        elif self.engine_name == 'sobol':
            return qmc.Sobol(d=self.dimension, scramble=True)
        elif self.engine_name == 'latin_hypercube':
            return qmc.LatinHypercube(d=self.dimension)
        else:
            raise ValueError("Unsupported engine type. Supported engines: 'halton', 'sobol', 'latin_hypercube'.")

    def sample(self, n_points):
        """Generates n_points samples."""
        return self.engine.random(n_points)

# Example usage
if __name__ == "__main__":
    sampler = QuasiMonteCarloSampler(dimension=3, engine='halton')
    samples = sampler.sample(5)
    print(samples)
