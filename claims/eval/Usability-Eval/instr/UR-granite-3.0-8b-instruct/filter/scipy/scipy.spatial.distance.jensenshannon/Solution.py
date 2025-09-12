import numpy as np
from scipy.spatial.distance import jensenshannon

def compute_jensen_shannon_distance(p, q):
    """
    Compute the Jensen-Shannon distance between two probability arrays.

    Parameters:
    p (numpy.ndarray): The first probability array.
    q (numpy.ndarray): The second probability array.

    Returns:
    float: The Jensen-Shannon distance between the two probability arrays.
    """
    # Ensure that the input arrays are valid probability distributions
    assert np.allclose(np.sum(p), 1), "p is not a valid probability distribution"
    assert np.allclose(np.sum(q), 1), "q is not a valid probability distribution"

    # Compute the Jensen-Shannon divergence
    jsd = jensenshannon(p, q)

    # Return the square root of the Jensen-Shannon divergence
    return np.sqrt(jsd)
