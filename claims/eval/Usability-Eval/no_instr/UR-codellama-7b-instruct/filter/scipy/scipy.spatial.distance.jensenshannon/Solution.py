
import numpy as np
from scipy.stats import entropy

def jensen_shannon_distance(p, q):
    """
    Compute the Jensen-Shannon distance (metric) between two probability arrays.

    Args:
        p (array): The first probability array.
        q (array): The second probability array.

    Returns:
        float: The Jensen-Shannon distance between p and q.
    """
    # Compute the entropies of p and q
    H_p = entropy(p)
    H_q = entropy(q)

    # Compute the Jensen-Shannon divergence
    D = 0.5 * (H_p - H_q) + 0.5 * np.log(2) + np.log(np.sqrt((2 * H_p - H_q) / (2 * H_p - H_q)))

    # Return the square root of the Jensen-Shannon divergence as the Jensen-Shannon distance
    return np.sqrt(D)
