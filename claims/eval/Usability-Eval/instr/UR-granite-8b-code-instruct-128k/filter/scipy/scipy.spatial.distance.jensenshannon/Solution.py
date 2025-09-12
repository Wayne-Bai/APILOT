from scipy.spatial.distance import jensenshannon
import numpy as np

# Define two probability arrays
p = np.array([0.1, 0.2, 0.3, 0.4])
q = np.array([0.4, 0.3, 0.2, 0.1])

# Compute the Jensen-Shannon distance
distance = jensenshannon(p, q)

# Print the Jensen-Shannon distance
print("The Jensen-Shannon distance between p and q is:", distance)
