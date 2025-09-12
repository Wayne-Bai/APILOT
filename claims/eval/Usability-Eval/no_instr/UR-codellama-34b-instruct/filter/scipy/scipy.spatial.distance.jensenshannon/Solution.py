import numpy as np
from scipy.stats import entropy

def jsd(p, q):
    """Compute the Jensen-Shannon distance between two probability arrays."""
    m = (p + q) / 2
    return np.sqrt(entropy(m, p) + entropy(m, q))
