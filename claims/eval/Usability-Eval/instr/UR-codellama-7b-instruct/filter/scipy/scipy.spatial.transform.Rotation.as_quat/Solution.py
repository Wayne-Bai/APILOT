import numpy as np
from scipy.spatial import Quaternion

# Create a quaternion object from a scalar and three vector components
q = Quaternion(scalar=1, vector=(2, 3, 4))

# Print the quaternion in a human-readable format
print(q)
