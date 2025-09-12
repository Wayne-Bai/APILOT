import numpy as np
from scipy.spatial.distance import jensenshannon

def jensen_shannon_distance(p, q):
    # Ensuring the probability distributions are numpy arrays
    p = np.asarray(p)
    q = np.asarray(q)

    # Calculate Jensen-Shannon Divergence
    divergence = 0.5 * jensenshannon(p, q)**2

    # The Jensen-Shannon distance is the square root of the Jensen-Shannon Divergence
    jsd = np.sqrt(divergence)

    return jsd
