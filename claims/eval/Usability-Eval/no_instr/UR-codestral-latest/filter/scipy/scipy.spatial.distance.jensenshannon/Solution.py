import numpy as np
from scipy import special, linalg

def jensen_shannon_distance(p, q):
    # Ensure probabilities sum to 1
    p = np.asarray(p) / np.sum(p)
    q = np.asarray(q) / np.sum(q)
    m = 0.5 * (p + q)
    return np.sqrt(0.5 * (special.entropy(p, m) + special.entropy(q, m)))

# Example usage:
p = [0.1, 0.4, 0.5]
q = [0.6, 0.1, 0.3]
distance = jensen_shannon_distance(p, q)
print(f'Jensen-Shannon distance: {distance}')
