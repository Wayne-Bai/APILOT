from scipy.special import entrop
from scipy.spatial.distance import pdist, squareform
import numpy as np

def jensen_shannon_distance(p, q):
    # Check if inputs are valid probability arrays
    if not np.isclose(np.sum(p), 1) or not np.isclose(np.sum(q), 1):
        raise ValueError("Inputs must be valid probability arrays")

    # Calculate the symmetric average of p and q
    m = (p + q) / 2

    # Calculate the Jensen-Shannon divergence
    js_divergence = 0.5 * entrop(p) + 0.5 * entrop(q) - entrop(m)

    # Return the square root of the Jensen-Shannon divergence as the distance
    return np.sqrt(js_divergence)

# Example usage
p = np.array([0.1, 0.2, 0.3, 0.4])
q = np.array([0.2, 0.3, 0.1, 0.4])
print(jensen_shannon_distance(p, q))
