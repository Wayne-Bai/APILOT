from scipy import stats
import numpy as np

# Define the two probability arrays
p = np.array([0.3, 0.4, 0.2, 0.1])
q = np.array([0.35, 0.25, 0.15, 0.1])

# Compute the Jensen-Shannon distance between the two arrays
jse_dist = stats.jensenshannon(p, q)

# Print the result
print("Jensen-Shannon Distance:", jse_dist)
