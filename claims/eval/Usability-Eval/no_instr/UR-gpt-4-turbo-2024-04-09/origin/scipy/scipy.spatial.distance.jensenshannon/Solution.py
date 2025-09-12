import numpy as np
from scipy.spatial.distance import jensenshannon

def compute_js_distance(p, q):
    return jensenshannon(p, q)

# Example usage:
p = np.array([0.3, 0.7])
q = np.array([0.4, 0.6])

js_distance = compute_js_distance(p, q)
print("Jensen-Shannon Distance:", js_distance)
