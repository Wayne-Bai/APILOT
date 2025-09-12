
import numpy as np
from scipy.spatial.distance import jensenshannon

# Define two probability arrays
p = np.array([0.2, 0.5, 0.3])
q = np.array([0.1, 0.6, 0.3])

# Calculate Jensen-Shannon distance
def jensen_shannon_distance(p, q):
    return np.sqrt(jensenshannon(p, q))

distance = jensen_shannon_distance(p, q)
print("Jensen-Shannon distance between the two arrays:", distance)
