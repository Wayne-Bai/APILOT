import numpy as np
from scipy.stats.qmc import QMCEngine

class GenericQMCSampler(QMCEngine):
    def __init__(self, d, seed=None):
        super().__init__(d=d, seed=seed)
        self.rng = np.random.default_rng(seed)
        # additional initialization can be performed here

    def random(self, n=1):
        """Generate n samples from the QMC engine."""
        samples = self.rng.random((n, self.d))
        return self._random(samples)

    def _random(self, samples):
        """Private method to modify samples. Can be overridden in subclasses."""
        return samples  # modify as needed or use as is

    def reset(self):
        """Reset the engine to its initial state."""
        super().reset()  # ensures the QMC engine is reset correctly
        self.rng = np.random.default_rng(self.seed)

# Example subclassing to create a specific sampler
class CustomQMCSampler(GenericQMCSampler):
    def _random(self, samples):
        """Customize the sampling strategy here."""
        # Implement some transformation or computation on samples
        return np.sqrt(samples)  # example transformation

# Example usage:
if __name__ == "__main__":
    d = 5  # dimension
    n = 10  # number of samples
    seed = 123
    sampler = CustomQMCSampler(d=d, seed=seed)
    samples = sampler.random(n)
    print("Generated Samples:")
    print(samples)
