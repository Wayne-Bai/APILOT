
from scipy import stats
import numpy as np

def weighted_gmean(a, weights):
    """Compute the weighted geometric mean along the specified axis."""
    a = np.array(a)
    weights = np.array(weights)
    return stats.gmean(a * weights, axis=None) / stats.gmean(weights, axis=None)
