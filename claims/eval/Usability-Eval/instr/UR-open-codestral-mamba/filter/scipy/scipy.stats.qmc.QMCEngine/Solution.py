import scipy.stats as stats
import numpy as np

class QuasiMonteCarlo:

  def __init__(self, bounds: list, dimensions: int):
    """
    Create a new quasi-Monte Carlo sampler.

    Arguments
    ---------
    bounds : list
      A list of tuples specifying the lower and upper bounds of the input
      dimensions.
    dimensions : int
      Number of output dimensions.
    """
    self.bounds = bounds
    self.dim = dimensions
    self.state = np.random.mtrand._rand

  def sample(self, num_samples: int):
    """
    Generate a Monte Carlo sample.

    Arguments
    ---------
    n_samples : int
      The number of samples to generate.
    """
    characteristics = []

    for i in range(num_samples):
      sample = []
      for min_b, max_b in self.bounds:
        sample.append(
          min_b + (max_b - min_b) * self.state.random()
        )

      characteristics.append(sample)

    return np.array(characteristics)
