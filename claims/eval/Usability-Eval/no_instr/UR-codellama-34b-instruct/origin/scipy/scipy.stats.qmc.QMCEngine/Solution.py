
import numpy as np
from scipy import integrate

class QMC:
    """A generic Quasi-Monte Carlo sampler class meant for subclassing."""

    def __init__(self, n_samples):
        self.n_samples = n_samples

    def sample(self, distribution):
        raise NotImplementedError("Subclasses must implement this method.")
