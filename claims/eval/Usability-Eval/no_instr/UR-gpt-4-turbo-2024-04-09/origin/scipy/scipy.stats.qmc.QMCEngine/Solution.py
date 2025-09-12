import scipy.stats as stats
import numpy as np

class QuasiMonteCarloSampler:
    def __init__(self, dist='uniform', parameters=None, seed=None):
        """
        Initializes the Quasi-Monte Carlo Sampler with a specified distribution.
        
        Args:
        dist (str or scipy.stats.rv_continuous): Distribution used for sampling. Either a string or a distribution object from scipy.stats.
        parameters (dict, optional): Parameters for the distribution. Defaults depend on the distribution.
        seed (int, optional): Seed for the random state to ensure reproducibility.
        """
        self.random_state = np.random.RandomState(seed)
        
        if isinstance(dist, str):
            if dist.lower() == 'uniform':
                self.dist = stats.uniform
            elif dist.lower() == 'normal':
                self.dist = stats.norm
            else:
                try:
                    self.dist = getattr(stats, dist.lower())
                except AttributeError:
                    raise ValueError(f"Unsupported distribution: {dist}")
        else:
            self.dist = dist

        self.parameters = parameters if parameters else {}

    def sample(self, size=1):
        """
        Generates random samples from the Quasi-Monte Carlo sequence.

        Args:
        size (int): Number of samples to generate.
        
        Returns:
        numpy.ndarray: Sampled values.
        """
        low_discrepancy_sample = self.dist(**self.parameters).rvs(size=size, random_state=self.random_state)
        return low_discrepancy_sample
