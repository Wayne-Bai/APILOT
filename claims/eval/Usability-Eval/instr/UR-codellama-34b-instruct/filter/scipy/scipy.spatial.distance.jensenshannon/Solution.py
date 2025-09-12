
import numpy as np
from scipy.spatial import distance

# Define the two probability arrays
p1 = np.array([0.2, 0.3, 0.5])
p2 = np.array([0.4, 0.3, 0.3])

# Compute the Jensen-Shannon divergence
js_divergence = distance.jensenshannon(p1, p2)

# Compute the Jensen-Shannon distance (metric)
js_distance = np.sqrt(js_divergence)

print("Jensen-Shannon distance:", js_distance)
