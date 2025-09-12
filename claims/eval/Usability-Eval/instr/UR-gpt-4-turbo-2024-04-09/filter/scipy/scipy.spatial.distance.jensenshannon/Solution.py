import numpy as np
from scipy.spatial.distance import jensenshannon

# Define probability distributions
p = np.array([0.1, 0.4, 0.5])
q = np.array([0.3, 0.4, 0.3])

# Compute the Jensen-Shannon distance
js_distance = jensenshannon(p, q)

print("Jensen-Shannon Distance:", js_distance)
