from scipy.spatial.distance import jensenshannon
import numpy as np

# Define probability arrays
p = np.array([0.3, 0.7])
q = np.array([0.4, 0.6])

# Compute Jensen-Shannon distance
distance = jensenshannon(p, q)

distance
