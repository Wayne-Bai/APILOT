import numpy as np
from scipy.spatial.distance import jensenshannon

def jensen_shannon_distance(p, q):
    """Compute the Jensen-Shannon distance between two probability arrays."""
    return jensenshannon(p, q, base=2)  # Using base 2 for divergence

# Example usage
p = np.array([0.1, 0.9])
q = np.array([0.5, 0.5])
distance = jensen_shannon_distance(p, q)
print("Jensen-Shannon distance:", distance)
