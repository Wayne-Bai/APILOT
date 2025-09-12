import numpy as np
from scipy.spatial.distance import jensenshannon

def jensen_shannon_distance(p, q):
    # Ensure the arrays sum to 1
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    
    # Normalize if necessary
    if not np.isclose(np.sum(p), 1.0):
        p /= np.sum(p)
    if not np.isclose(np.sum(q), 1.0):
        q /= np.sum(q)
    
    # Compute the Jensen-Shannon distance
    js_distance = jensenshannon(p, q)
    
    return js_distance

# Example usage
p = [0.1, 0.4, 0.5]
q = [0.5, 0.3, 0.2]

distance = jensen_shannon_distance(p, q)
print(f"Jensen-Shannon distance: {distance}")
